import pandas as pd

def classify(age):
    if age<18:
        return "Child"
    else:
        return "Adult"
df=pd.read_excel("data/titanic.xlsx")
df["Age_group"]=df["Age"].apply(classify)
print(df[["Age","Age_group"]])