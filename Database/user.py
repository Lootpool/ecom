import sqlite3

conn=sqlite3.connect("users.db")
cur=conn.cursor()
cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(25) NOT NULL,email VARCHAR(25) NOT NULL)")
conn.commit()
conn.close()