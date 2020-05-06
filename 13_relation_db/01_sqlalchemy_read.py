from sqlalchemy import create_engine
import pandas as pd

data = pd.read_csv ('../csv_data/input.csv')
print('data:')
print (data)

# create the database engine
engine = create_engine ('sqlite:///:memory:')

# Store the dataframe as a table
data.to_sql ('data_table', engine)

# Query 1 one the relational database
res1 = pd.read_sql_query ('SELECT * FROM data_table', engine)
print ('\nres1: SELECT * FROM data_table')
print(res1)

# Query 2 one the relational database
res2 = pd.read_sql_query ('SELECT id, name, salary FROM data_table', engine)
print ('\nres2: SELECT id, name, salary FROM data_table')
print(res2)

# Query 3 on the relational database
res3 = pd.read_sql_query ('SELECT id, dept, salary FROM data_table group by dept', 
engine)
print('\nres3: SELECT id, dept, salary FROM data_table group by dept')
print (res3)

# Query 4 on the relational database
res4 = pd.read_sql_query ('SELECT id, dept,sum(salary) FROM data_table group by dept', 
engine)
print('\nres4: SELECT id, dept,sum(salary) FROM data_table group by dept')
print (res4)
