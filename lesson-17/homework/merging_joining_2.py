import pandas as pd
import numpy as np
df_1=pd.read_csv("data/movie.csv")[["director_name", "color"]]
df_2=pd.read_csv("data/movie.csv")[["director_name", "num_critic_for_reviews"]]
left_join=pd.merge(df_1,df_2,on="director_name",how="left")
outer_join=pd.merge(df_1,df_2,on="director_name",how="outer")
row_1=len(df_1)
row_2=len(df_2)
print("Number of rows for left join: ",row_1)
print("Number of rows for full outer join: ",row_2)