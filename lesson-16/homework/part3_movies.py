import pandas as pd
import numpy as np

#Identify the director with the highest total director_facebook_likes.
df_movies=pd.read_csv("data/movie.csv")
sorted_df_movies=df_movies.sort_values(by="director_facebook_likes",ascending=False)
row=sorted_df_movies.head(1)
print(row["director_name"])

#Find the 5 longest movies and their respective directors.
sorted_df_movies_byd=df_movies.sort_values(by="duration",ascending=False)
rows=sorted_df_movies_byd.head(5)
print(rows[["movie_title","director_name"]])