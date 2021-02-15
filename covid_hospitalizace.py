import requests
import pandas as pd


def download(url):
    data_set = requests.get(url)
    return data_set


def json_grab(data_set):
    data_json = data_set.json()
    return data_json


def data_frame(data_json):
    df = pd.DataFrame(data_json['data'])
    return df


def stat(df):
    print(df.describe())


def main(url):
    data_set = download(url)
    data_json = json_grab(data_set)
    df = data_frame(data_json)

    stat(df)

    print(df)


if __name__ == '__main__':
    URL_HOSP = \
        'https://' \
        'onemocneni-aktualne.mzcr.cz/api/v2/covid-19/hospitalizace.json'

    URL_CONFIRMED_TESTU = \
        'https://' \
        'onemocneni-aktualne.mzcr.cz/api/v2/covid-19/' \
        'nakazeni-vyleceni-umrti-testy.json'

    main(URL_HOSP)
