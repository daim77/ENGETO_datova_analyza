import sqlalchemy
import pandas as pd


# user = "student"
# password = "p7@vw7MCatmnKjy7"
# conn_string = f"mysql+pymysql://{user}:{password}@data.engeto.com/data"
# alchemy_conn = sqlalchemy.create_engine(conn_string)

# data = pd.read_sql('countries', alchemy_conn, parse_dates=True)
# data.to_csv('tables/countries.csv')



df = pd.DataFrame(pd.read_csv('tables/countries.csv'))
# print(df['population'].sum())

moje_data = pd.concat([
    df[(df['landlocked'] == 1)].groupby(['continent'])['country'].count(),
    df[(df['landlocked'] == 1)].groupby(['continent'])['population'].sum(),
    df[(df['landlocked'] == 1)].groupby(['continent'])['surface_area'].sum()
], axis=1)

moje_data['popul density'] = \
    round(moje_data['population'] / moje_data['surface_area'], 0)
moje_data.name = 'landlocked'

print(moje_data)

# notes.to_csv('tables/group_by1.csv')
