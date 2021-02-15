import requests
import pandas as pd
from pprint import pprint as pp
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

    print(df_cumul['death'].tail())

    df = df_cumul.diff(axis=0)
    df['date'] = df_cumul['date']
    df.to_csv('covid_cz_diff.csv')
    return df


def stat(df):
    print(df.describe())
    print(df[(df['confirmed'] > 10000)].count())


def draw_df(df):
    df['confirmed'] = df['confirmed'].rolling(7).mean()

    df.plot(y="confirmed", color='black')
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
    URL_HOSP = \
        'https://' \
        'onemocneni-aktualne.mzcr.cz/api/v2/covid-19/hospitalizace.json'

    URL_CONFIRMED_TESTU = \
        'https://' \
        'onemocneni-aktualne.mzcr.cz/api/v2/covid-19/' \
        'nakazeni-vyleceni-umrti-testy.json'

    main(URL_CONFIRMED_TESTU)
