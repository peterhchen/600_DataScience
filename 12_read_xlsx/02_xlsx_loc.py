import pandas as pd
data = pd.read_excel ('../xlsx_data/input.xlsx')

print ("data.loc[[1, 3, 5], ['salary', 'name']:")
print (data.loc[[1, 3, 5], ['salary', 'name']])