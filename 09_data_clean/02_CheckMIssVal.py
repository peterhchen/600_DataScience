import pandas as pd
import numpy as np
df = pd.DataFrame (np.random.randn(5, 3), 
index =['a', 'c', 'd', 'e', 'h'], columns= ['one', 'two', 'three'])

df = df.reindex (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print("df['one'].isnull()")
print(df['one'].isnull())
