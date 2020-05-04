import pandas as pd
data = { 'Name': ['Peter', 'Irene', 'Jason', 'Jasmine'], 'Age': [62, 54, 29, 26]}
df = pd.DataFrame (data, index = ['rank1', 'rank2', 'rank3', 'rank4'])
print ('df:'); print(df)
# df:
#           Name  Age
# rank1    Peter   62
# rank2    Irene   54
# rank3    Jason   29
# rank4  Jasmine   26