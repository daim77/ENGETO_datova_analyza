import requests
import pandas as pd
from pprint import pprint as pp


def download(url):
    data_set = requests.get(url)
    return data_set


def json_grab(data_set):
    data_json = data_set.json()
    return data_json


def data_frame(data_json):
    df_cumul = pd.DataFrame(data_json['data'])
    df_cumul['datum'] = pd.to_datetime(df_cumul['datum'])
    df = df_cumul.diff(axis=0)
    df['datum'] = df_cumul['datum']
    df.to_csv('covid_cz_diff.csv')
    return df


def stat(df):
    print(df.columns)
    print(df.dtypes)
    print(df.describe())

# {'datum': '2021-02-14',
#            'kumulativni_pocet_ag_testu': 2044626,
#            'kumulativni_pocet_nakazenych': 1090860,
#            'kumulativni_pocet_testu': 4944403,
#            'kumulativni_pocet_umrti': 18250,
#            'kumulativni_pocet_vylecenych': 969154}


def main(url):
    data_set = download(url)
    data_json = json_grab(data_set)
    df = data_frame(data_json)

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
