import pandas as pd

df_iris=pd.read_json("data/iris.json")
print(df_iris.describe())
