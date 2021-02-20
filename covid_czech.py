import requests
import csv

import pandas as pd
import matplotlib.pyplot as plt


def download_data(url):
    data_set = requests.get(url)
    if data_set.status_code != 200:
        print('Failed to get data:', data_set.status_code)
    else:
        return data_set.json()


def download_data_csv(url):
    data_set = requests.get(url)
    if data_set.status_code != 200:
        print('Failed to get data:', data_set.status_code)
    else:
        wrapper = csv.reader(data_set.text.split('\n'))
        return pd.DataFrame(wrapper)


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


def data_frame_3(df):
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    df = df.rename({'﻿datum': 'date'}, axis=1)

    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    df['upv_kapacita_volna'] = pd.to_numeric(df['upv_kapacita_volna'])
    df = df.groupby(df.index)['upv_kapacita_volna'].sum()
    df = pd.DataFrame(df)
    df.columns = ['ventilation_available']
    df = df.astype({'ventilation_available': int})

    return df


def join_data(df_1, df_2, df_3):
    # df = pd.merge(df_1, df_2, left_index=True, right_index=True)
    # df = pd.merge(df, df_3, left_index=True, right_index=True)
    df = pd.concat([df_1, df_2, df_3], axis=1)
    return df


def stat(df):
    print('=' * 82)
    print('Last DATA: ')
    print('=' * 82)
    print(df.tail(8))
    print('=' * 82)

    print('DATA description: ')
    print('=' * 82)
    print(df[df.index > pd.to_datetime('2021-01-01')].describe().round(2))
    print('=' * 82)

    print('days with more than 10.000 confirmed: ')
    print('=' * 82)
    print(df[(df['confirmed'] > 10000)].count())
    print('=' * 82)
    print('=' * 82)


def draw_df(df):
    days = 7  # plovouci prumer za XY dni
    df['confirmed'] = df['confirmed'].rolling(days).mean()
    df['test'] = df['test'].rolling(days).mean()
    df['death'] = df['death'].rolling(days).mean()
    df['ag_test'] = df['ag_test'].rolling(days).mean()
    df['in_hosp'] = df['in_hosp'].rolling(days).mean()
    df['ventilation_available'] = \
        df['ventilation_available'].rolling(days).mean()

    df.plot(
        y=[
            "confirmed", 'test', 'death', 'ag_test', 'in_hosp',
            'ventilation_available'
        ],
        color=['red', '#F29010', 'black', '#F2D410', '#663300', 'blue'],
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
    df_zoomed = df.loc['20201101':]

    df_zoomed.plot(
        y=["confirmed", 'death', 'in_hosp', 'ventilation_available'],
        color=['red', 'black', '#663300', 'blue'],
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

    data_from_csv = download_data_csv(
        'https://dip.mzcr.cz/api/v1/'
        'kapacity-intenzivni-pece-vlna-2.csv'
    )
    df_3 = data_frame_3(data_from_csv)

    df = join_data(df_1, df_2, df_3)

    stat(df)
    draw_df(df)
    draw_df_zoomed(df)


if __name__ == '__main__':
    main()
