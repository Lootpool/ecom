import sqlite3

conn=sqlite3.connect("orders.db")
cur=conn.cursor()
cur.execute("CREATE TABLE orders(oid INTEGER PRIMARY KEY AUTOINCREMENT,uid INTEGER,pid INTEGER,qty INTEGER)")
conn.commit()
conn.close()