import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('deci6.xlsx', sheet_name="Sheet1")

df = pd.DataFrame(df)

df['Percentile Rank'] = df.deci.rank(method='first', pct=True)
df['Decile Rank'] = pd.qcut(df['Percentile Rank'], 10, labels=False)
df.to_excel("deci6_output.xlsx")