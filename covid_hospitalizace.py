import requests
import pandas as pd
import matplotlib.pyplot as plt


def download(url):
    data_set = requests.get(url)
    return data_set


def json_grab(data_set):
    data_json = data_set.json()
    return data_json


def data_frame(data_json):
    df_cumul = pd.DataFrame(data_json['data'])
    df_cumul.columns = [
        'date', 'confirmed', 'recovered', 'death', 'test', 'ag_test'
    ]
    df_cumul['date'] = pd.to_datetime(df_cumul['date'])

    df = df_cumul.diff(axis=0)
    df['date'] = df_cumul['date']

    df.to_csv('covid_cz_diff.csv')
    return df


def stat(df):
    print('Last DATA: ')
    print(df.tail(8))
    print('=' * 60)

    print(df[df['date'] > pd.to_datetime('2021-01-01')].describe().round(2))
    print('=' * 60)

    print(df[(df['confirmed'] > 10000)].count())
    print('=' * 60)


def draw_df(df):
    Q = 7  # plovouci prumer za Q dni
    df['confirmed'] = df['confirmed'].rolling(Q).mean()
    df['test'] = df['test'].rolling(Q).mean()
    df['death'] = df['death'].rolling(Q).mean()
    df['ag_test'] = df['ag_test'].rolling(Q).mean()

    df.plot(
        x='date', y=["confirmed", 'test', 'death', 'ag_test'],
        color=['red', 'blue', 'black', 'cyan']
    )

    plt.yscale('log')
    plt.title('Day increment')

    plt.savefig('log_confirmed.png')
    plt.savefig('log_confirmed.svg', format='svg', dpi=1200)

    plt.show()


def main(url):
    data_set = download(url)
    data_json = json_grab(data_set)
    df = data_frame(data_json)
    draw_df(df)

    stat(df)


if __name__ == '__main__':
    URL_CONFIRMED_TESTU = \
        'https://' \
        'onemocneni-aktualne.mzcr.cz/api/v2/covid-19/' \
        'nakazeni-vyleceni-umrti-testy.json'

    main(URL_CONFIRMED_TESTU)
