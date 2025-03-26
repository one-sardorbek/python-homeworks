import pandas as pd

df=pd.read_csv("data/movie.csv")
grouped_data=df.groupby(["color","director_name"]).agg(
    Total_num_critic_for_reviews=("num_critic_for_reviews","count"),
    Avg_duration=("duration","mean")
).reset_index()
print(grouped_data)