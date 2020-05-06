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

# Insert another row
sql.execute ('INSERT INTO data_table VALUES(?,?,?,?,?,?)', 
engine, params=[('index-8',9,'Peter',1000.00,'2020-05-06','IT')])
sql.execute ('INSERT INTO data_table VALUES(?,?,?,?,?,?)', 
engine, params=[('index-9',10,'Irene',800.00,'2020-05-07','Service')])

# Query 1 one the relational database
res1 = pd.read_sql_query ('SELECT * FROM data_table', engine)
print ('\nres1: SELECT ID,Dept,Name,Salary, Start_date FROM data_table')
print(res1)
