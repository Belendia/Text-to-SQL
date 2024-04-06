import sqlite3

## connect to sqlite
connection = sqlite3.connect('student.db')

## create a cursor object to insert record, create table, retrieve records
cursor = connection.cursor()

## create the table
student_table = '''
    create table student
        (
            name varchar(25)),
            class varchar(25),
            section varchar(25),
            marks int
        );
    '''
cursor.execute(student_table)

### Insert some more records
cursor.execute("insert into student values('John', 'Data Science', 'A', 90)")
cursor.execute("insert into student values('Marta', 'Data Science', 'B', 80)")
cursor.execute("insert into student values('Rahel', 'Data Science', 'B', 85)")
cursor.execute("insert into student values('Tarin', 'DevOps', 'A', 100)")
cursor.execute("insert into student values('Kurma', 'DevOps', 'B', 70)")

## Display all the records
print('The inserted records are')
data = cursor.execute('''select * from student''')

for row in data:
    print(row)

## close the connection
connection.commit()
connection.close()
