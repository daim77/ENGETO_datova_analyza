# https://stackoverflow.com/questions/10951341/pandas-dataframe-aggregate-function-using-multiple-columns

# https://pbpython.com/weighted-average.html

import pandas as pd
import numpy as np


sales = pd.read_excel("https://github.com/chris1610/pbpython/blob/master/data/"
                      "sales-estimate.xlsx?raw=True", sheet_name="projections")

