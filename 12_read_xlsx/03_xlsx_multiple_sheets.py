import pandas as pd
with pd.ExcelFile ('../xlsx_data/input.xlsx') as xlsx:
    df1 = pd.read_excel (xlsx, 'Sheet1')
    df2 = pd.read_excel (xlsx, 'Sheet2')

print ("df1[0:5]['salary']:")
print (df1[0:5]['salary'])
print ("\ndf2[0:5]['ziocode']:")
print (df2[0:5]['zipcode'])