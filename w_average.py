# https://stackoverflow.com/questions/10951341/pandas-dataframe-aggregate-function-using-multiple-columns

# https://pbpython.com/weighted-average.html

import pandas as pd
import numpy as np


def w_avg(df, avg_column, weight_column):
    try:
        return (df[avg_column] * df[weight_column]).sum() \
               / df[weight_column].sum()
    except ZeroDivisionError:
        return df[avg_column].mean()


if __name__ == '__main__':

    sales = pd.read_excel("https://github.com/chris1610/pbpython"
                          "/blob/master/data/"
                          "sales-estimate.xlsx?raw=True",
                          sheet_name="projections")

    print(sales.Current_Price.mean())
    print(sales['Current_Price'].mean())
    print(sales['Current_Price'].mean() == sales.Current_Price.mean())  # True

    # weighted average METHOD I
    w_a_1 = (sales.Current_Price * sales.Quantity).sum() / sales.Quantity.sum()

    # fce groupby
    mean_by_manager = sales.groupby('Manager')['Current_Price'].mean()
    mean_by_manager_I = sales.groupby('Manager').Current_Price.mean()

    # weighted average METHOD II
    w_a_2 = sales.groupby('Manager').apply(w_avg, 'Current_Price', 'Quantity')
    w_a_3 = sales.groupby(["Manager", "State"])\
        .apply(w_avg, "New_Product_Price", "Quantity")

    # multiple aggregation
    f = {'New_Product_Price': ['mean'],
         'Current_Price': ['median'],
         'Quantity': ['sum', 'mean']}
    agg_1 = sales.groupby("Manager").agg(f)
    agg_2 = sales.groupby("Manager").apply(lambda x: pd.Series({
        'mean_new_product_price': np.average(x.New_Product_Price),
        'median_current_price': np.median(x.Current_Price),
        'sum_quantity': x.Quantity.sum(),
        'mean_quantity': x.Quantity.mean(),
        'wa_new_product_price': w_avg(x, 'New_Product_Price', 'Quantity'),
        'wa_current_price': w_avg(x, 'Current_Price', 'Quantity')
    }))

    # weighted average METHOD III
    w_a_4 = sales.groupby("Manager").apply(
        lambda x: np.average(x['New_Product_Price'], weights=x['Quantity']))
