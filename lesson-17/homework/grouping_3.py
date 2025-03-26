import pandas as pd

df=pd.read_parquet("data/flights")
grouped_df=df.groupby(["Year","Month"]).agg(
    total_flights=("flights","count"),
    Avg_arrdelay=("ArrDelay","mean"),
    Max_depdelay=("DepDelay","max")
)
print(grouped_df)
