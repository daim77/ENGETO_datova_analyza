import pandas as pd

import sqlalchemy


user = "student"
password = "p7@vw7MCatmnKjy7"
conn_string = f"mysql+pymysql://{user}:{password}@data.engeto.com/data"
alchemy_conn = sqlalchemy.create_engine(conn_string)

# table_names = [
#     'covid19_basic_differences',
#     'covid19_basic',
#     'covid19_detail_us',
#     'covid19_detail_us_differences',
#     'covid19_detail_global',
#     'covid19_detail_global_differences', 'lookup_table'
# ]
# for t in table_names:
#     df = pd.read_sql(t, alchemy_conn, parse_dates=True)
#     df.to_csv(f'tables/{t}.csv')

df = pd.read_csv('tables/covid19_basic_differences.csv')

# print(df.head(10))
# print(df.tail(10))
#
print(df.shape)
# print(len(df.index))
# print(len(df.columns))
#
# print(df.columns)
#
# print(df.info)
# print(df.dtypes)
#
# print(df.describe())
# print(
#     df[
#         (df['confirmed'] > 0) & (df['deaths'] > 0) & (df['recovered'] > 0)
#         ].describe()
# )

df_cz = pd.DataFrame(df[
    (df['country'] == 'Czechia')
    & (df['confirmed'] > 0)
    & (df['deaths'] > 0)
    & (df['recovered'] > 0)
].reset_index())

df_cz = df_cz.drop(columns=['country']).set_index('date')
df_cz = df_cz.drop(columns=['index'])

print(df_cz[(df_cz['confirmed'] > 10000)].count())

# print(df_cz)
