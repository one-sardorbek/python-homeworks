import pandas as pd

df_movies=pd.read_csv("data/movie.csv")
print(df_movies.sample(10))
