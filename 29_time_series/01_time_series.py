from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../csv_data/google_stock.csv')
df = pd.DataFrame(data, columns = ['Date', 'Close'])

# Set the Date as Index
df['Date'] = pd.to_datetime(df['Date'])
df.index = df['Date']
del df['Date']

df.plot(figsize=(15, 6))
plt.show()
