import pandas as pd, time, json

df = pd.read_csv("../data/POS.csv")

for _, row in df.iterrows():
    event = {"timestamp": row[0], "transaction": 1}
    print(json.dumps(event))
    time.sleep(1)
