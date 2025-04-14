from flask import * 
import sqlite3
import requests

app=Flask(__name__)



@app.route("/addorder",methods=["POST"])
def add_order():
    data=request.json
    id=data["id"]
    pid=data["pid"]
    pQty=data["pQty"]
    try:
        conn=sqlite3.connect("./Database/orders.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO orders(uid,pid,qty) VALUES(?,?,?)",(id,pid,pQty))
        conn.commit()
        conn.close()
        return jsonify({"success":True,"msg":"INSERTED ORDER"}),200
    except Exception as e:
        return jsonify({"success":False,"msg":"ORDER SERVICE"+str(e)}),200

@app.route("/vieworder",methods=["GET"])
def view_order():
    data=request.json
    oid=data["oid"]
    try:
        conn=sqlite3.connect("./Database/orders.db")
        conn.row_factory=sqlite3.Row
        cur=conn.cursor()
        cur.execute("SELECT * FROM orders WHERE oid=?",(oid,))
        row=cur.fetchone()
        result=dict(row)
        conn.commit()
        conn.close()
        return jsonify({"success":True,"data":result}),200
    except Exception as e:
        return jsonify({"success":False,"msg":"ORDER SERVICE"+str(e)}),200
    
def main():
    app.run(debug=True,host="0.0.0.0",port=10000)
if __name__=='__main__':
    main()
