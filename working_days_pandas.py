import pandas as pd
import numpy as np


link = 'https://en.wikipedia.org/wiki/Workweek_and_weekend'
tables = pd.read_html(link)
df = tables[2].iloc[:, :4]

df.drop(df.loc[:, ['Typical hours worked per week', 'Typical hours worked '
                                                    'per day']], axis=1,
        inplace=True)

working_days_df = df.rename(
    columns={'Nation': 'country', 'Working week': 'working_days'}
)
# split rubbish
working_days_df['working_days'] = working_days_df['working_days'].str.split(
    r"\ |\[|\(", n=0).str[0]

working_days_df['working_days'] = \
    np.where(
        working_days_df['working_days'] != 'Monday–Friday', 'diff', 'regular')

print('Pocet statu s odlisnym vikendem: ',
      working_days_df[working_days_df['working_days'] == 'diff'].shape[0])
