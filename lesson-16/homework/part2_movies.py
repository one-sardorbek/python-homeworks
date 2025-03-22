import pandas as pd

df_movies=pd.read_csv("data/movie.csv")
filtered_df_movies=df_movies[df_movies["duration"] > 120]
sorted_df_movies=df_movies.sort_values(by="director_facebook_likes",ascending=False)
