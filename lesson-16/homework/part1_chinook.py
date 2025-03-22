import pandas as pd
import sqlite3


with sqlite3.connect("data/chinook.db") as connection:
    df_employee=pd.read_sql(
       " SELECT * FROM customers",
       con=connection
       )
print(df_employee.head(10))
 