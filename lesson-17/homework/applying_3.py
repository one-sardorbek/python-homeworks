import pandas as pd

def classify_dur(duration):
    if duration < 60:
        return "Short"
    if duration > 60 and duration < 120:
        return "Medium"
    if duration > 120:
        return "Long"
        
df=pd.read_csv("data/movie.csv")
df["Classify_duration"]=df["duration"].apply(classify_dur)
print(df[["duration","Classify_duration"]])