import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy import inspect


# file1 = open('/Users/martindanek/Documents/programovani/engeto_password.txt', "r")
# user_data = eval(file1.read())
# file1.close()
#
# user = user_data[0][0]
# password = user_data[0][1]
#
# conn_string = f"mysql+pymysql://{user}:{password}@data.engeto.com/data"
# engeto_conn = sqlalchemy.create_engine(conn_string, echo=True)
#
# countries_e_df = pd.read_sql('countries', engeto_conn, parse_dates=True)

user = "xxx"
password = "xxx"
conn_string = f"mysql+pymysql://{user}:{password}@lamikoko.cz/lamikokocz1"

lamikoko_conn = sqlalchemy.create_engine(conn_string, echo=True)

# countries_e_df.to_sql('countries_II', lamikoko_conn)

# inspector = inspect(lamikoko_conn)
# schemas = inspector.get_schema_names()
#
# for schema in schemas:
#     print(f'schema: {schema}')
#     for table_name in inspector.get_table_names(schema=schema):
#         print(f'table names: {table_name}')
#         # for column in inspector.get_columns(table_name, schema=schema):
#         #     print("Column: %s" % column)


countries_df = pd.read_sql(
    'countries', lamikoko_conn, parse_dates=True)
# print(countries_df.shape)

# covid_df = pd.read_sql(
#     'covid19_basic_differences', lamikoko_conn, parse_dates=True)

# ===== WHERE UKOL 2 ====
# df = pd.read_sql_query("SELECT "
#                        "country, date, confirmed "
#                        "FROM covid19_basic_differences "
#                        "WHERE country = 'Austria' ", lamikoko_conn)
# print(df.dropna())

# df = covid_df.query("country == 'Austria'")[['date', 'country', 'confirmed']]
# print(df.dropna())

# cond = covid_df.country == 'Austria'
# df = covid_df.loc[cond, ['date', 'country', 'confirmed']]
# print(df.dropna())


# df = countries_df[['country', 'currency_name']]
# cond1 = df.dropna().currency_name.str.contains('Dollar')
# print(df.dropna()[cond1])
