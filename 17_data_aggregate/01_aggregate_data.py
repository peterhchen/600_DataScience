import pandas as pd
import numpy as np

# Generate 10 x 4 matrix
df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print('df:')
print(df)

r = df.rolling(window=3,min_periods=1)
print('r:')
print(r)

# Perform aggregate for all columns
# Take the sum with window=3 for the data: 
# A[0]= A[0], A[1] = A[0] + A[1], A[2] = A[0]+A[1]+A[2], 
# A[3] = A[1] + A[2] + A[3], and etc.
print ('np.sum:')
print (np.sum)
print ('r.aggregate (np.sum):')
print (r.aggregate (np.sum))

# Perform the aggregate column 'A'
print ("r['A'].aggregate (np.sum):")
print (r['A'].aggregate (np.sum))
# perform the aggregate for 'A' and 'B'.
print ("r['A', 'B'].aggregate (np.sum):")
print (r['A', 'B'].aggregate (np.sum))