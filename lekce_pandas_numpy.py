import numpy as np
import pandas as pd
from pprint import pprint as pp

import sqlalchemy as db


# def classify_population(value_list):
#     output = []
#     for r in value_list:
#         if r <= 20:
#             output.append('small')
#         else:
#             output.append('large')
#     return output
#
#
#
# values_lst = [[11, 79], [66, 243], [196, 924]]
# # print(values_lst[0])
# #
# # population = []
# # for row in values_lst:
# #     population.append(row[0])
# # print(population)
# #
# # population = []
# # population = [row[0] for row in values_lst]
# # print(population)
#
# values_array = np.array(values_lst)
#
# # pp(values_array)
# # print(values_array.shape)
# # pp(values_array[0])
# # pp(values_array[:, 0])
# # pp(np.sum(values_array[:, 0]))  # mean, median atd...
#
# print(np.sum(values_array, axis=0))
# print(np.sum(values_array, axis=1))
#
# # pop_class = ['large' for item in values_lst if item[0] >=20 else 'small']
#
# print(np.where(values_array[:, 0] <= 20, 'small', 'large')) # podminka v numpy
#
#
# pop_big_arr = np.random.randint(0, 100, size=10000000)
# print(np.where(pop_big_arr <=20, 'small', 'large'))
#
# pop_big_nonvec_class = classify_population(pop_big_arr)
# pp(pop_big_nonvec_class)

user = "student"
password = "p7@vw7MCatmnKjy7"
conn_string = f"mysql+pymysql://{user}:{password}@data.engeto.com/data"
engeto_conn = db.create_engine(conn_string, echo=True)

db_connection = engeto_conn.connect()

df_country = pd.read_sql_query(
    'select * '
    'from countries as c',
    engeto_conn, parse_dates=True
)

db_connection.close()

print(df_country.set_index('country').head())

print(df_country.index)
print(type(df_country.values))

# lze DataFrame z pandas konvertovat do np.array kvuli vykonu and v.v.

pp(df_country.columns)

srs = df_country['country']  # dve zavorky jsou pak pandas df not series
print(type(srs))
print(srs)

df_select = df_country[['country', 'capital_city', 'continent']]
# pp(df_select.set_index('country', inplace=True))


# vyber radku .loc[], iloc[]
# row_selection = ['Czech Republic', 'Slovakia']
# pp(df_select.loc[row_selection])
pp(df_select.iloc[[10, 50, 75]])

row_select_1 = ['Czech Republic', 'Slovakia']
col_select_1 = ['national_dish']
# pp(df_country.loc[row_select_1, col_select_1])  # a podobne iloc

pp(df_country.isna().sum())

col_selection = ['continent', 'currency_code', 'domain_tld']
df = df_country[col_selection]
print(df[df.isna().any(axis=1)])

# # nan lze zahodit
# pp(df.shape)
# # df.dropna()  # parametr thresh=1 napr.
# # df_1 = df.dropna(thresh=1)
# df_1 = df.dropna()
# pp(df_1.shape)

# nan nahradit hodnotou
# col_select = ['elevation', 'life_expectancy']
# df = df_country[col_select]
# # df.fillna(100)  # value, prumerem, medianem atd...
# elev_mean = df['elevation'].dropna().mean()
# pp(df['elevation'].fillna(elev_mean))

# nahradi predchozi hodnotou - pouzitelne pro casove rady
# df.fillna(method='ffill')  # forward fill
# df.fillna(method=bfill)   # backward fill


# jak zahodit sloupec nebo radek

# df_country.drop('Afghanistan')  # je to jako inplace na radek

# df_country.drop('avg_height', axis=1, inplace=False)

# # nastaveni multiindexu
# df_country.set_index('country', inplace=True)
# df = df_country.set_index('continent', append=True).swaplevel().sort_index()
# pp(df.loc['Europe'])
# pp(df.loc[('Europe', 'Czech Republic')])
# pp(df.index)
#
# # podminky aka WHERE
# pp(df_country.query("continent == 'Europe'"))
# df_country.query("country in ('Czech Republic', 'Slovakia')")

# popisne statistiky
pp(df_country[['population', 'surface_area']].describe())
pp(df_country.info())
