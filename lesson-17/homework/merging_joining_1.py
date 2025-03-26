import sqlite3
import pandas as pd
with sqlite3.connect("data/chinook.db") as connection:
    df_customers = pd.read_sql("SELECT * FROM customers", con=connection)
    df_invoices = pd.read_sql("SELECT * FROM invoices", con=connection)
join=pd.merge(df_customers,df_invoices,on="CustomerId",  suffixes=('_cust', '_inv'))

invoice_counts = df_invoices.groupby("CustomerId").size().reset_index(name="TotalInvoices")

# Merge with customer data to include names
result = pd.merge(df_customers, invoice_counts, on="CustomerId", how="left")

# Select relevant columns (CustomerId, Name, TotalInvoices)
result = result[["CustomerId", "FirstName", "LastName", "TotalInvoices"]]

# Display the result
print(result)