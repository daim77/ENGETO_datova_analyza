import requests
import pandas as pd
import matplotlib.pyplot as plt


def download_data(url):
    data_set = requests.get(url)
    return data_set.json()


def data_frame_1(data_json):
    df = pd.DataFrame(data_json['data'])
    df.columns = [
        'date', 'confirmed', 'recovered', 'death', 'test', 'ag_test'
    ]
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    df = df.diff(axis=0)
    df.to_csv('covid_cz_diff.csv')
    return df


def data_frame_2(data_json):
    df = pd.DataFrame(data_json['data'])
    df = df.rename({'pocet_hosp': 'in_hosp', 'datum': 'date'}, axis=1)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    df.drop(
        df.columns[[num for num in range(15) if num != 2]],
        axis=1, inplace=True)

    df.to_csv('covid_cz_hosp.csv')
    return df


def join_data(df_1, df_2):
    df = pd.merge(df_1, df_2, left_index=True, right_index=True)
    return df


def stat(df):
    print('Last DATA: ')
    print(df.tail(8))
    print('=' * 60)
    print(df[df.index > pd.to_datetime('2021-01-01')].describe().round(2))
    print('=' * 60)

    print(df[(df['confirmed'] > 10000)].count())
    print('=' * 60)


def draw_df(df):
    Q = 7  # plovouci prumer za Q dni
    df['confirmed'] = df['confirmed'].rolling(Q).mean()
    df['test'] = df['test'].rolling(Q).mean()
    df['death'] = df['death'].rolling(Q).mean()
    df['ag_test'] = df['ag_test'].rolling(Q).mean()
    df['in_hosp'] = df['in_hosp'].rolling(Q).mean()

    df.plot(
        y=["confirmed", 'test', 'death', 'ag_test', 'in_hosp'],
        color=['red', 'blue', 'black', 'cyan', '#663300'],
        use_index=True
    )
    plt.yscale('log')

    plt.ylabel('log')
    plt.xlabel('')
    plt.title('Covid in Czech')

    plt.savefig('log_confirmed.png')
    plt.savefig('log_confirmed.svg', format='svg', dpi=1200)

    plt.show()


def draw_df_zoomed(df):
    df_zoomed = df.loc['20210101':]

    df_zoomed.plot(
        y=["confirmed", 'test', 'death', 'ag_test', 'in_hosp'],
        color=['red', 'blue', 'black', 'cyan', '#663300'],
        use_index=True
    )
    plt.yscale('log')

    plt.ylabel('log')
    plt.xlabel('')
    plt.title('Covid in Czech - zoomed')

    plt.savefig('log_confirmed_zoom.png')
    plt.savefig('log_confirmed_zoom.svg', format='svg', dpi=1200)

    plt.show()


def main():
    data_json = download_data(
        'https://'
        'onemocneni-aktualne.mzcr.cz/api/v2/covid-19/'
        'nakazeni-vyleceni-umrti-testy.json'
    )
    df_1 = data_frame_1(data_json)

    data_json = download_data(
        'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/'
        'hospitalizace.json'
    )
    df_2 = data_frame_2(data_json)

    df = join_data(df_1, df_2)

    stat(df)
    draw_df(df)
    draw_df_zoomed(df)


if __name__ == '__main__':
    main()
