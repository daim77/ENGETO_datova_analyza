import pandas as pd
import numpy as np


living_df = pd.read_csv(
    'London_living/London_living.csv', delimiter=';', decimal=','
)

print(living_df.head(3))

# download tables from wiki with pandas - using lxml modul by default
# SSL certificate problem - update command.certificate in macOS python dir
link = 'https://en.wikipedia.org/wiki/London_boroughs'
tables = pd.read_html(link)
df = tables[2].iloc[:, :2]
designations_df = df.copy()

designations_df.loc[:, 'London borough']\
    .replace({'Hammersmith[notes 2]': 'Hammersmith and Fulham',
              'Barking[notes 3]': 'Barking and Dagenham'}, inplace=True)

# designations_df.rename(columns={'London borough': 'Area'}, inplace=True)

# join, merge, concatenate
# merged_df = living_df.merge(designations_df, how='left')
#
# living_df.set_index('Area', inplace=True)
# designations_df.set_index('Area', inplace=True)
# joined_df = living_df.join(designations_df)

merged_df = pd.merge(living_df, designations_df,
                     how='left', left_on='Area', right_on='London borough')\
    .set_index('Area')\
    .drop('London borough', axis=1)

merged_df['safety_travel_weighted'] = \
    np.round((2 * merged_df.safety + merged_df.travel) / 3, 2)

merged_df.assign(rent_per_w=lambda x: x.Rent_per_m / 4,
                 gree_dichotomous=
                 np.where(merged_df.green_spec >= 0.5, 'green', 'not_green'),
                 safety_squared=lambda y: y.safety ** 2).round(2)

