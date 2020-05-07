import pandas as pd
df1 = pd.DataFrame ({
    'lkey': [1,2,3,4,5,6],
    'Name': ['Peter', 'Irene', 'Jessica', 'Jason', 'Jasmine', 'Jonathan'],
    'subject_id': ['sub1','sub2', 'sub3','sub4','sub5','sub6']
})
df2 = pd.DataFrame ({
    'rkey': [1,2,3,4,5,6],
    'Name': ['Ming', 'Li', 'Arthur', 'Max', 'Min', 'Cap'],
    'subject_id': ['sub2','sub4', 'sub3','sub6','sub5','sub1']
})
print('df1:')
print(df1)
print('df2:')
print(df2)
df3 = df1.merge(df2, left_on='lkey', right_on='rkey')
print('df3:')
print(df3)