import pandas as pd

df = pd.read_csv('data/clusters.csv')
df.to_json('data/clusters.json', orient='index')
