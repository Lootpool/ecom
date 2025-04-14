from flask import * 
import sqlite3
import requests

app=Flask(__name__)

AUTH_SERVICE="http://localhost:5001"
ORDER_SERVICE="http://localhost:5002"
PRODUCT_SERVICE="http://localhost:5003"

@app.route("/add",methods=["POST"])
def add_product():
    data=request.json
    pName=data["pName"]
    pPrice=data["pPrice"]
    pQty=data["pQty"]
    try:
        conn=sqlite3.connect("./Database/products.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO products(name,price,stock) VALUES(?,?,?)",(pName,pPrice,pQty))
        conn.commit()
        conn.close()
        return jsonify({"success":True,"msg":"INSERTED PRODUCT"}),200
    except Exception as e:
        return jsonify({"success":False,"msg":"PRODUCT SERVICE"+str(e)}),200

@app.route("/delete",methods=["POST"])
def delete_product():
    data=request.json
    pId=data["pId"]
    try:
        conn=sqlite3.connect("./Database/products.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM products WHERE id=?",(pId,))
        conn.commit()
        conn.close()
        return jsonify({"success":True,"msg":"DELETED PRODUCT"}),200
    except Exception as e:
        return jsonify({"success":False,"msg":"PRODUCT SERVICE"+str(e)}),200

@app.route("/update",methods=["POST"])
def update_product():
    data=request.json
    pId=data["pId"]
    pName=data["pName"]
    pPrice=data["pPrice"]
    pQty=data["pQty"]
    try:
        conn=sqlite3.connect("./Database/products.db")
        cur=conn.cursor()
        cur.execute("UPDATE products SET name=?,price=?,stock=? WHERE id=?",(pName,pPrice,pQty,pId))
        conn.commit()
        conn.close()
        return jsonify({"success":True,"msg":"DELETED PRODUCT"}),200
    except Exception as e:
        return jsonify({"success":False,"msg":"PRODUCT SERVICE"+str(e)}),200

@app.route("/viewproducts",methods=["GET"])
def view_products():
    try:
        conn=sqlite3.connect("./Database/products.db")
        conn.row_factory=sqlite3.Row
        cur=conn.cursor()
        cur.execute("SELECT * FROM products")
        rows=cur.fetchall()
        result=[]
        for row in rows:
            result.append(dict(row))
        conn.commit()
        conn.close()
        return jsonify({"success":True,"data":result}),200
    except Exception as e:
        return jsonify({"success":False,"msg":"PRODUCT SERVICE"+str(e)}),200



def main():
    app.run(debug=True,host="0.0.0.0",port=5003)
if __name__=='__main__':
    main()