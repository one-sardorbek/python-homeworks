import pandas as pd

def filter_survivers(df):
    return df[df["Survived"]==1]
def filling_age(df):
    return df.assign(Age=df["Age"].fillna(df["Age"].mean()))
def Fare_Per_Age(df):
    return df.assign(Fare_Per_Age=df["Fare"] / df["Age"])

df=pd.read_excel("data/titanic.xlsx")
df_new=(
    df.pipe(filter_survivers)
      .pipe(filling_age)
      .pipe(Fare_Per_Age)
)
print(df_new)