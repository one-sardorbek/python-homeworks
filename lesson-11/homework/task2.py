import sqlite3
#Creating
with sqlite3.connect("library.db") as data:
    cursor=data.cursor()
    queary="""DROP TABLE IF EXISTS Books;
    CREATE TABLE Books
    (Title TEXT, Author TEXT, Year_Published INT,Genre TEXT)"""
    cursor.executescript(queary)
#Inserting data 
insert_data=(
     ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
     ("1984","George Orwell", 1949,	"Dystopian"), 
     ("The Great Gatsby","F. Scott Fitzgerald", 1925,"Classic")   
 )
with sqlite3.connect("library.db") as data:
    cursor=data.cursor()
    cursor.executemany("INSERT INTO Books VALUES(?, ?, ?, ?)", insert_data)
#Updating data
with sqlite3.connect("library.db") as data:
    cursor=data.cursor()
    query="UPDATE Books SET Year_Published=1950 where Title='1984'"   
    cursor.executescript(query)
#Displaying Dystopian genres
with sqlite3.connect("library.db") as data:
    cursor=data.cursor() 
    queary="SELECT Title, Author FROM Books where Genre = 'Dystopian'"
    data=cursor.execute(queary)
print(data.fetchall())
#Adding column Rating
with sqlite3.connect("library.db") as data:
    cursor=data.cursor() 
    add="Alter table Books ADD column Rating FLOAT"
    cursor.execute(add)
    cursor.execute("UPDATE Books SET Rating=4.8 where Title='To Kill a Mockingbird'")
    cursor.execute("UPDATE Books SET Rating=4.7 where Title='1984'")
    cursor.execute("UPDATE Books SET Rating=4.5 where Title='The Great Gatsby'")
#Sorting
with sqlite3.connect("library.db") as data:
    cursor=data.cursor() 
    queary="Select * from Books order by Year_Published desc"
    sorted_data=cursor.execute(queary)
print(sorted_data.fetchall())
#Deleting data
with sqlite3.connect("library.db") as data:
    cursor=data.cursor() 
    queary="DELETE FROM Books where Year_Published < 1950"
    cursor.execute(queary)