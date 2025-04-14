import sqlite3

conn=sqlite3.connect("products.db")
cur=conn.cursor()
cur.execute("CREATE TABLE products(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(25) NOT NULL,price FLOAT NOT NULL,stock INTEGER NOT NULL)")
conn.commit()
conn.close()