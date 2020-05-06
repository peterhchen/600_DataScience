import pandas as pd
import numpy as np

df = pd.DataFrame ({'one': [10, 20, 30, 40, 50, 1000],
'two': [2000, 0, 50, 60, 70, 80]})

print('df.replace({1000:10, 2000:20}')
print(df.replace({1000:10, 2000:20}))