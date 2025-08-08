import sqlite3
try :
    a=sqlite3.connect('demo.db')
    print('Database connected')
except Exception as e:
    print(e)

tbl_cr='create table vrinda (id int,name text, course text)'789+
try:
    a.execute(tbl_cr)
    print('table created !')
except Exception as e:
    print(e)

