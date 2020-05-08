import pandas as pd
# Create a Dictionary of series
d = {
   'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 
   'Smith', 'Jack', 'Lee', 'Chanchal', 'Gasper', 
   'Naviya', 'Andres']),
   'Age': pd.Series([25, 26, 25, 23, 30, 
   23, 23, 34, 40, 30, 
   25, 46]),
   'Rating': pd.Series ([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 
   3.8, 3.8, 3.78, 2.98, 4.80, 
   4.10, 3.65])
}
# Create a DataFrame
df = pd.DataFrame (d)
# Calculate the standard devication
print('df.skew():')
print(df.skew())