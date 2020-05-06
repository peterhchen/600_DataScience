# Read row and column with loc
import pandas as pd
data = pd.read_csv ('../csv_data/input.csv')

print ("\ndata.loc[[1, 3, 5], ['salary', 'name']:")
print (data.loc[[1, 3, 5], ['salary', 'name']])