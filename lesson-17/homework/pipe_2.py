import pandas as pd

def filter_flights(df):
    return df[df["DepDelay"] > 30]
def Delay_Per_Hour(df):
    return df.assign(Delay_Per_Hour=df["DepDelay"] / df["duration"])

df=pd.read_parquet("data/flights")
df_new=(
    df.pipe(filter_flights)
      .pipe(Delay_Per_Hour)  
)
print(df_new.head())
print(df.columns)