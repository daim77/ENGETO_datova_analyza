import pandas as pd
import numpy as np

import sqlalchemy as db
import matplotlib.pyplot as plt


file1 = open('/Users/martindanek/Documents/programovani/engeto_password.txt', "r")
user_data = eval(file1.read())
file1.close()

user = user_data[0][0]
password = user_data[0][1]

conn_string = f"mysql+pymysql://{user}:{password}@data.engeto.com/data"
engeto_conn = db.create_engine(conn_string, echo=True)

# načteme a seznámíme se s tabulkou economies
# vhodně upravíme datové typy, nastavíme indexy
# spočítáme HDP na osobu
# zobrazíme časové řady HDP na osobu a porodnosti ve vybraných státech

economies_df = pd.read_sql('economies', engeto_conn, parse_dates=True)
print(economies_df.info())
# rok je typ object - to je spatne
economies_df = economies_df\
    .assign(year=economies_df.year.astype(int))\
    .set_index(['country', 'year'])

economies_df['GDP_per_capita'] = np.round(economies_df.GDP / economies_df.population, 2)

# sloupce co nas zajima
cols = ['GDP', 'GDP_per_capita', 'population', 'fertility']
economies_df = economies_df[cols]
# === UKOL
states_selection = ['Czech Republic', 'Slovakia', 'Ukraine', 'Romania']
df = economies_df.loc[states_selection, ['GDP_per_capita']]
# chci nyni ve sloupci rok jako index, country do sloupce s GDP_per_capita
# df = df.unstack(level=0).sort_index(ascending=False)  # ma stale multiindex
df = df.unstack(level=0).sort_index(ascending=False).dropna()
print(type(df))
df.plot()  # proc nekresli graf?

countries_df = pd.read_sql('countries', engeto_conn, parse_dates=True)
countries_df = countries_df[['country', 'continent', 'region_in_world', 'population']]

# economies_df.query('year == 2015').reset_index('year').drop('year', 1)
# economies_df.query('year == 2015').droplevel('year')
economies_df = economies_df.swaplevel().loc[2015]

# nyni tabulky spojime
pd.merge(countries_df, economies_df, on='country', how='inner')

# join je pres index, je potreba je nastavit= podporuje dobrou pripravu tabulek
countries_df = countries_df.set_index('country')
df2 = countries_df.join(economies_df, rsuffix='econ').set_index('continent', append=True).swaplevel().loc['Europe']
df2.head()

simple_mean = df2.groupby('region_in_world')[['GDP_per_capita']].mean().round()

wa = pd.DataFrame(df2\
    .dropna(subset=['GDP_per_capita', 'population'])\
    .groupby('region_in_world')\
    .apply(lambda x: np.average(x.GDP, weights=x.population))\
    .round())
simple_mean.rename(columns={'GDP_per_capita': 'simple_evg'}).join(wa)

# UKOL

religions_df = pd.read_sql('religions', engeto_conn, parse_dates=True, index_col=['year', 'country']).drop('region', 1).loc[2010]

df4 = religions_df.groupby('country').sum().rename(columns={'population': 'total_popul'})
religions_df = religions_df.join(df4)
religions_df['religion_ratio'] = np.round(religions_df.population / religions_df.total_popul * 100, 2)
# religions_df = countries_df.set_index('country')[['continent']].join(religions_df)
states = ['Czech Republic']
srs = religions_df.loc[states, ['religion_ratio']]
religions_df['religion'].unique()
srs = religions_df.query('total_popul > 5000000').groupby('country')['religion_ratio'].std().dropna().sort_values()
srs.plot.bar()

# visualni analyza
edf = economies_df.loc[:, ['GDP_per_capita', 'fertility']].dropna()
edf.plot.scatter('GDP_per_capita', 'fertility', figsize=(10, 8), s=80, marker='o', edgecolors='k', color='r')

le_df = pd.read_sql('life_expectancy', engeto_conn, index_col=['year', 'country']).loc[2010, ['life_expectancy']]
df = countries_df.join(le_df).join(edf).dropna()
df.plot.scatter('GDP_per_capita', 'life_expectancy', marker='x')

# histogram

df = countries_df.join(edf).dropna()
df['GDP_per_capita'].hist(bins=30)
plt.show()

# logaritmicka transformace
df = countries_df.join(edf).dropna()
np.log(df['GDP_per_capita']).hist(bins=30)
plt.show()

df = countries_df.set_index('country').join(economies_df[['GDP', 'GDP_per_capita']])
df =