import pandas as pd
import numpy as np

import sqlalchemy as db


user = "student"
password = "p7@vw7MCatmnKjy7"
conn_string = f"mysql+pymysql://{user}:{password}@data.engeto.com/data"
engeto_conn = db.create_engine(conn_string, echo=True)

# db_connection = engeto_conn.connect()

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

# db_connection.close()

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
selection = countries_df['religion'].isin(['Buddhism', 'Hinduism'])  # vraci boolean
print(countries_df[selection])
np.unique(countries_df.loc[selection, 'religion'], return_counts=True)

