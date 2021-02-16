import pandas as pd


living_df = pd.read_csv(
    'London_living/London_living.csv', delimiter=';', decimal=','
)

print(living_df.head(3))


link = 'https://en.wikipedia.org/wiki/London_boroughs'
tables = pd.read_html(link)

print(tables)
