# Read row and column with loc
import pandas as pd
data = pd.read_csv ('../csv_data/input.csv')
print ("data.loc[:, ['salary', 'name']:")
print (data.loc[:, ['salary', 'name']])
print ("\ndata.loc[:5, ['salary', 'name']:")
print (data.loc[:5, ['salary', 'name']])