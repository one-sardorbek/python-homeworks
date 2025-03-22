import pandas as pd
import numpy as np

df_flights=pd.read_parquet("data/flights")
new_columns = [column.lower() for column in df_flights.columns]
df_flights.columns=new_columns
#print(df_flights[["origin","dest"]]) #there is no column named carrier
df_selected = df_flights[['origin', 'dest']]
print(df_selected)

unique_destinations = df_flights['dest'].nunique()
print(f"Number of unique destinations: {unique_destinations}")