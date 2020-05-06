import pandas as pd
data = pd.read_json ('../json_data/input.json')
print("data.to_json(orient='record', lines=True)")
print(data.to_json(orient='records', lines=True))
