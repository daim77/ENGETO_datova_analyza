import sqlalchemy
import pandas as pd


user = "student"
password = "p7@vw7MCatmnKjy7"
conn_string = f"mysql+pymysql://{user}:{password}@data.engeto.com/data"
alchemy_conn = sqlalchemy.create_engine(conn_string)

table_names = [
    'covid19_basic_differences',
    'covid19_basic',
    'covid19_detail_us',
    'covid19_detail_us_differences',
    'covid19_detail_global',
    'covid19_detail_global_differences', 'lookup_table'
]
for t in table_names:
    df_t = pd.read_sql(t, alchemy_conn, parse_dates=True)
    df_t.to_csv(f'tables/{t}.csv')

