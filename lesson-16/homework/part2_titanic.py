import pandas as pd
import numpy as np

df_titanic=pd.read_excel("data/titanic.xlsx")
filtered_df_titanic=df_titanic[df_titanic["Age"] > 30]
male_arr=np.where(df_titanic["Sex"] == "male")
female_arr=np.where(df_titanic["Sex"] == "female")
male_value_counts=len(male_arr[0])
female_value_counts=len(female_arr[0])
print(female_value_counts)
print(male_value_counts)
print(filtered_df_titanic)