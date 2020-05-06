from sqlalchemy import create_engine
from pandas.io import sql
import pandas as pd

data = pd.read_csv ('../csv_data/input.csv')
print('data:')
print (data)

# create the database engine
engine = create_engine ('sqlite:///:memory:')

# Store the dataframe as a table
data.to_sql ('data_table', engine)

# Query 1: Delete row from data_table
sql.execute ('DELETE FROM data_table WHERE name = (?)', 
engine, params=[('Gary')])
res1 = pd.read_sql_query ('SELECT ID,Dept,Name,Salary,Start_date FROM data_table', 
engine)
print ('\nres1: SELECT ID,Dept,Name,Salary,Start_date FROM data_table')
print(res1)

# Query 2: Delete row from data_table
sql.execute ('DELETE FROM data_table WHERE name = (?)', 
engine, params=[('Guru')])
res2 = pd.read_sql_query ('SELECT ID,Dept,Name,Salary,Start_date FROM data_table', 
engine)
print ('\nres2: SELECT ID,Dept,Name,Salary,Start_date FROM data_table')
print(res2)
