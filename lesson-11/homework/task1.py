import sqlite3
#Creating
with sqlite3.connect("Rosters.db") as data:
    cursor=data.cursor()
    queary="""DROP TABLE IF EXISTS roster;
    CREATE TABLE roster 
    (Name TEXT, Species TEXT, Age INT)"""
    cursor.executescript(queary)
#Inserting data 
insert_data=(
     ("Benjamin Sisko",	"Human",40),
     ("Jadzia Dax","Trill",	300), 
     ("Kira Nerys","Bajoran", 29)   
 )
with sqlite3.connect("Rosters.db") as data:
    cursor=data.cursor()
    cursor.executemany("INSERT INTO roster VALUES(?, ?, ?)", insert_data)
#Updating data
with sqlite3.connect("Rosters.db") as data:
    cursor=data.cursor()
    query="UPDATE roster SET Name='Ezri Dax' where Name='Jadzia Dax'"   
    cursor.executescript(query)
#Displaying Bajoran species
with sqlite3.connect("Rosters.db") as data:
    cursor=data.cursor() 
    queary="SELECT Name, Age FROM roster where Species = 'Bajoran'"
    data=cursor.execute(queary)
print(data.fetchall())
#Adding column Rank
with sqlite3.connect("Rosters.db") as data:
    cursor=data.cursor() 
    add="Alter table roster ADD column Rank TEXT"
    cursor.execute(add)
    cursor.execute("UPDATE roster SET Rank='Major' where Name='Kira Nerys'")
    cursor.execute("UPDATE roster SET Rank='Lieutenant' where Name='Ezri Dax'")
    cursor.execute("UPDATE roster SET Rank='Captain' where Name='Benjamin Sisko'")
#Sorting
with sqlite3.connect("Rosters.db") as data:
    cursor=data.cursor() 
    queary="Select * from roster order by Age desc"
    sorted_data=cursor.execute(queary)
print(sorted_data.fetchall())
#Deleting data
with sqlite3.connect("Rosters.db") as data:
    cursor=data.cursor() 
    queary="DELETE FROM roster where age > 100"
    cursor.execute(queary)