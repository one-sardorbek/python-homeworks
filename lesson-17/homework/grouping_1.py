import pandas as pd

df=pd.read_excel("data/titanic.xlsx")
grouped_data=df.groupby("Pclass").agg(
    Avg_Age=("Age", "mean"),      # Calculate average age
    Total_Fare=("Fare", "sum"),   # Calculate total fare
    Passenger_Count=("Pclass", "count")  # Count passengers
).reset_index()
print(grouped_data)