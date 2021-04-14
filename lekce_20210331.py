import pandas as pd
import numpy as np

import sqlalchemy as db


file1 = open('/Users/martindanek/Documents/programovani/engeto_password.txt', "r")
user_data = eval(file1.read())
file1.close()

user = user_data[0][0]
password = user_data[0][1]

conn_string = f"mysql+pymysql://{user}:{password}@data.engeto.com/data"
engeto_conn = db.create_engine(conn_string, echo=True)

countries_df = pd.read_sql('countries', engeto_conn, parse_dates=True)

# df = pd.read_sql_query(
#     "SELECT cd.date, cd.country, lt.iso3, cd.confirmed "
#     "FROM covid19_basic_differences as cd "
#     "LEFT OUTER JOIN lookup_table lt "
#     "ON cd.country = lt.country AND lt.province is null "
#     "WHERE cd.country='Czechia' "
#     "AND MONTH(date)=10 ",
#     engeto_conn, parse_dates=True
# )


# print(countries_df.head())
# # podminky
# print(countries_df.query("religion == 'Buddhism'").shape)
#
# print(countries_df.loc[1])  # radkovy index
# countries_df.sample(frac=0.1)  # nahodny vyber 10% tabulky
#
# selection = np.random.binomial(1, 0.1, size=countries_df.shape[0]).astype(bool)
# print(selection)  #  toto chci pro vyber radku, kde je True
# print(countries_df.loc[selection])  # vyber 10% nahodnych radku


# df = countries_df.copy()  # jedine s copy odkazuji na jiny objekt
# selection = (df['religion'] == 'Buddhism').to_numpy()
# print(df[selection])

# =====
# print(countries_df['independence_date'])
# countries_df.query("independence_date < 1500")[['country', 'independence_date']].sort_values('independence_date')

# selection = countries_df.independence_date < 1500
# print(countries_df.loc[selection, ['country', 'independence_date']].sort_values('independence_date'))

# =====
# selection = countries_df['religion'].isin(['Buddhism', 'Hinduism'])  # vraci boolean
# print(countries_df[selection])
# print(np.unique(countries_df.loc[selection, 'religion'], return_counts=True))
#
# print(countries_df.query("religion not in ('Christianity', 'Islam')"))

# selection = ~countries_df.religion.isin(['Cristianity', 'Islam'])  # tilda u vektoru jede jako NOT
# print(selection)
# print(countries_df[selection])
#
# cond1 = ~countries_df.religion.isin(['Christianity', 'Islam'])
# cond2 = ~countries_df.religion.isna()
# selection = cond1 & cond2
# print(countries_df[selection])  # dve podminky

# # prvni zpusob
# print(countries_df.query("currency_code == 'EUR' and religion != 'Christianity'"))
#
# # druhy zpusob
# cond1 = countries_df.currency_code == 'EUR'
# cond2 = countries_df.religion != 'Christianity'
# print(countries_df[cond1 & cond2])  # and nefunguje musi byt &

# # ===
# cond1 = countries_df.religion == 'Christianity'
# cond2 = countries_df.continent == 'Asia'
# cond3 = countries_df.religion == 'Islam'
# cond4 = countries_df.continent == 'Europe'
#
# cond11 = cond1 & cond2
# cond12 = cond3 & cond4
#
# selection = cond11 | cond12
#
# print(countries_df[selection])
# print(countries_df.loc[selection, ['country', 'continent', 'religion']])


# tvorba novych sloupcu

# countries_df['new_column'] = 1  # a rovnou ho naplnim cislem => vytvori sloupec
#
# countries_df = countries_df.assign(new_new_column=2)  # musim priradit puvodni objekt
#
# print(countries_df['new_new_column'].head())

# countries_df = countries_df.assign(manual_popdens=countries_df.population / countries_df.surface_area)
# print(countries_df)


# def celsius_to(data):  # do funkce lze posilat celou DataFrame
#     return 9/5 * data + 32
#
#
# countries_df['yat_fahrenheit'] = celsius_to(countries_df.yearly_average_temperature)
# nebo rovnou s fci apply
# countries_df.yearly_average_temperature.apply(celsius_to)

# GROUP BY
# print(countries_df[['continent', 'population']].groupby('continent').sum())
#
# print(
#     countries_df[['continent', 'population']].
#         groupby('continent').
#         agg({'population': lambda x: np.round(sum(x)/1000000, 1)}).
#         sort_values('population', ascending=False)
# )

# ====
# print(countries_df[['continent', 'surface_area']].groupby('continent').mean())

# ====
# print(countries_df[['continent', 'population']].groupby('continent').\
#     agg({'population': ['sum', 'mean', 'count']}))

# df = countries_df[['continent', 'religion', 'population']].\
#     groupby(['continent', 'religion']).sum()
# print(df)
# print(countries_df.query("continent == 'Africa and religion == 'Hinduism'"))

# vazeny prumer
df = countries_df[['country', 'continent', 'population', 'life_expectancy']]\
    .dropna()
wa = lambda x: np.average(x, weights=df.loc[x.index, 'population'])
# print(df.groupby('continent').agg({'life_expectancy': wa}))
# print(df.groupby('continent')[['life_expectancy']].mean())

df1 = df.groupby('continent').agg({'life_expectancy': [wa, 'mean']})
print(df1)
df2 = df.groupby('continent')\
    .apply(
    lambda x:
    pd.Series(
        {'wa': np.average(x.life_expectancy, weights=x.population),
         'mean': np.average(x.life_expectancy)}
    )
)
print(df2)


#
# print(
#     countries_df
#         .query("continent == 'Oceania'")
#     [['country', 'life_expectancy', 'population']]
#         .sort_values('life_expectancy', ascending=False)
# )

