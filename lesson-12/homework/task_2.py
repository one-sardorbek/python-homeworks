import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
job_listings = soup.find_all("div", class_="card-content")
    
jobs = []
for job in job_listings:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    application_link = job.find("a", text="Apply")['href']
        
    jobs.append((title, company, location, application_link))
with sqlite3.connect("database.db") as data:
    cursor=data.cursor()
    queary="""DROP TABLE IF EXISTS jobs;
    CREATE TABLE jobs
    (Job Title TEXT, Company Name TEXT, Location TEXT,Application Link TEXT)"""
    cursor.executescript(queary)

with sqlite3.connect("database.db") as data:
    cursor=data.cursor()
    queary="""INSERT INTO jobs VALUES(?,?,?,?)"""
    cursor.executemany(queary,jobs)
with sqlite3.connect("database.db") as data:
    cursor=data.cursor()
def filter_jobs(location=None, company=None):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")
    
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    
    return results
def export_to_csv(filename, location=None, company=None):
    jobs = filter_jobs(location, company)
    
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Title", "Company", "Location", "Application Link"])
        writer.writerows(jobs)
    
    print(f"Filtered job listings exported to {filename}")






