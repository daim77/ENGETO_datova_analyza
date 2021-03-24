import pandas as pd

import sqlalchemy as db


user = "student"
password = "p7@vw7MCatmnKjy7"
conn_string = f"mysql+pymysql://{user}:{password}@data.engeto.com/data"
alchemy_conn = db.create_engine(conn_string)

df = pd.read_sql('covid19_basic_differences', alchemy_conn, parse_dates=True)

print(df.head())