import sqlite3

try:
    con=sqlite3.connect("new.db")
    print("Database created/Connected")
except Exception as e:
    print(e)


#table creation 
tbl_create="create table studinfo(id integer primary key autoincrement, name text, course text)"
try:
    con.execute(tbl_create)
    print("Table Created!")
except Exception as e:
    print(e)

#insert data into table
insert_data="insert into studinfo(name, course)values('vrinda','bca'),('jiya','bba'),('kina','mca'),('krishna','llb')"
try:
    con.execute(insert_data)
    con.commit()
    print("Table Created!")
except Exception as e:
    print(e)

#delete 
"""delete_data="delete from studinfo where id=4"
try:
    con.execute(delete_data)
    con.commit()
    print("Table Created!")
except Exception as e:
    print(e)"""