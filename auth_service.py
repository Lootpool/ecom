from flask import * 
import sqlite3
import requests

app=Flask(__name__)

AUTH_SERVICE="http://localhost:5001"
ORDER_SERVICE="http://localhost:5002"
PRODUCT_SERVICE="http://localhost:5003"

@app.route("/login",methods=["POST"])
def login():
    data=request.json
    uName=data["uName"]
    uMail=data["uMail"]
    try:
        conn=sqlite3.connect("./Database/users.db")
        conn.row_factory=sqlite3.Row
        cur=conn.cursor()
        cur.execute("SELECT * FROM users WHERE name=? AND email=?",(uName,uMail))
        rows=cur.fetchone()
        conn.commit()
        conn.close()
        if(rows):
            return jsonify({"success":True}),200
        else:
            return jsonify({"success":False,"msg":"USER DOESN'T EXIST"}),200
    except Exception as e:
        return jsonify({"success":False,"msg":"AUTH SERVICE"+str(e)}),200

@app.route("/signup",methods=["POST"])
def signup():
    data=request.json
    uName=data["uName"]
    uMail=data["uMail"]
    try:
        conn=sqlite3.connect("./Database/users.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO users(name,email) VALUES(?,?)",(uName,uMail))
        conn.commit()
        conn.close()
        return jsonify({"success":True}),200
    except Exception as e:
        return jsonify({"success":False,"msg":"AUTH SERVICE"+str(e)}),200

def main():
    app.run(debug=True,host="0.0.0.0",port=5001)
if __name__=='__main__':
    main()