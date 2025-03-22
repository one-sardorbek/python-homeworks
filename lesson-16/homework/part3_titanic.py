import pandas as pd

df_titanic=pd.read_excel("data/titanic.xlsx")
minimum=df_titanic["Age"].min()
maximum=df_titanic["Age"].max()
sum=df_titanic["Age"].sum()
print(f"max={maximum}\nmin={minimum}\nsum={sum}")