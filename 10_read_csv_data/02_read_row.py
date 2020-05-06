import pandas as pd
data = pd.read_csv ('../csv_data/input.csv')
print ('data[0:5]:')
print (data[0:5])
print ("\ndata[0:5]['salary']:")
print (data[0:5]['salary'])