import pandas as pd
data = pd.read_json ('../json_data/input.json')
print ("data.loc[[1,3,5], ['Salary', 'Name']")
print (data.loc[[1,3,5], ['Salary', 'Name']])