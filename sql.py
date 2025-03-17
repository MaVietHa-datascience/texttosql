import sqlite3

#connect to sqllite
connection = sqlite3.connect("student.db")
## create cursor object to insert records, create table,retrieve
cursor = connection.cursor()
## create table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""
cursor.execute(table_info)

## Insert records

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

## Display all the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
