import pandas as pd

df_iris=pd.read_json("data/iris.json")
new_columns = [column.lower() for column in df_iris.columns]
df_iris.columns=new_columns
print(df_iris[["sepallength","sepalwidth"]])

