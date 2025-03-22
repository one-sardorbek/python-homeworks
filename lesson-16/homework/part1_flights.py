import pandas as pd

df_flights=pd.read_parquet("data/flights")
print(df_flights.info())