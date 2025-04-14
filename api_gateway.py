from flask import * 
import sqlite3
import requests

app=Flask(__name__)

AUTH_SERVICE="http://localhost:5001"
ORDER_SERVICE="http://localhost:5002"
PRODUCT_SERVICE="http://localhost:5003"

@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/loginpage",methods=["GET"])
def loginpage():
    return render_template("login_page.html")

@app.route("/login",methods=["POST"])
def login():
    uName=request.form["uName"]
    uMail=request.form["uMail"]
    try:
        response=requests.post(AUTH_SERVICE+"/login",json={"uName":uName,"uMail":uMail})
        if response.status_code==200:
            data=response.json()
            isValid=data["success"]
            if isValid:
                return viewUser(uName)
            else:
                return render_template("results.html",msg=data["msg"])
    except Exception as e:
        return render_template("results.html",msg=str(e))

@app.route("/signuppage",methods=["GET"])
def signuppage():
    return render_template("signup_page.html")

@app.route("/signup",methods=["POST"])
def signup():
    uName=request.form["uName"]
    uMail=request.form["uMail"]
    try:
        response=requests.post(AUTH_SERVICE+"/signup",json={"uName":uName,"uMail":uMail})
        if response.status_code==200:
            data=response.json()
            isValid=data["success"]
            if isValid:
                return viewUser(uName)
            else:
                return render_template("results.html",msg=data["msg"])
    except Exception as e:
        return render_template("results.html",msg=str(e))
    
@app.route("/addproductpage",methods=["GET"])
def add_productpage():
    return render_template("addproduct.html")

@app.route("/add",methods=["POST"])
def add_product():
    pName=request.form["pName"]
    pPrice=request.form["pPrice"]
    pQty=request.form["pQty"]
    try:
        response=requests.post(PRODUCT_SERVICE+"/add",json={"pName":pName,"pPrice":pPrice,"pQty":pQty})
        if response.status_code==200:
            data=response.json()
            print(data)
            isValid=data["success"]
            if isValid:
                return render_template("results.html",msg="SUCCESSFULLY INSERTED PRODUCT")
            else:
                return render_template("results.html",msg=data["msg"])
    except Exception as e:
        return render_template("results.html",msg=str(e))

@app.route("/deleteproductpage",methods=["GET"])
def delete_productpage():
    return render_template("deleteproduct.html")

@app.route("/delete",methods=["POST"])
def delete_product():
    pId=request.form["pId"]
    try:
        response=requests.post(PRODUCT_SERVICE+"/delete",json={"pId":pId})
        if response.status_code==200:
            data=response.json()
            print(data)
            isValid=data["success"]
            if isValid:
                return render_template("results.html",msg="SUCCESSFULLY DELETED PRODUCT")
            else:
                return render_template("results.html",msg=data["msg"])
    except Exception as e:
        return render_template("results.html",msg=str(e))

@app.route("/updateproductpage",methods=["GET"])
def update_productpage():
    return render_template("updateproduct.html")

@app.route("/update",methods=["POST"])
def update_product():
    pId=request.form["pId"]
    pName=request.form["pName"]
    pPrice=request.form["pPrice"]
    pQty=request.form["pQty"]
    try:
        response=requests.post(PRODUCT_SERVICE+"/update",json={"pName":pName,"pPrice":pPrice,"pQty":pQty,"pId":pId})
        if response.status_code==200:
            data=response.json()
            print(data)
            isValid=data["success"]
            if isValid:
                return render_template("results.html",msg="SUCCESSFULLY UPDATED PRODUCT")
            else:
                return render_template("results.html",msg=data["msg"])
    except Exception as e:
        return render_template("results.html",msg=str(e))

@app.route("/viewproducts",methods=["GET"])
def view_product():
    try:
        response=requests.get(PRODUCT_SERVICE+"/viewproducts")
        if response.status_code==200:
            data=response.json()
            print(data)
            isValid=data["success"]
            if isValid:
                return render_template("results.html",msg=data["data"])
            else:
                return render_template("results.html",msg=data["msg"])
    except Exception as e:
        return render_template("results.html",msg=str(e))
    
@app.route("/addorderpage",methods=["GET"])
def add_orderpage():
    return render_template("addorder.html")

@app.route("/addorder",methods=["POST"])
def add_order():
    id=request.form["id"]
    pid=request.form["pid"]
    pQty=request.form["qty"]
    try:
        response=requests.post(ORDER_SERVICE+"/addorder",json={"id":id,"pid":pid,"pQty":pQty})
        if response.status_code==200:
            data=response.json()
            print(data)
            isValid=data["success"]
            if isValid:
                return render_template("results.html",msg="SUCCESSFULLY INSERTED PRODUCT")
            else:
                return render_template("results.html",msg=data["msg"])
    except Exception as e:
        return render_template("results.html",msg=str(e))

@app.route("/vieworderpage",methods=["GET"])
def view_orderpage():
    return render_template("vieworderpage.html")

@app.route("/vieworder",methods=["POST"])
def view_order():
    oid=request.form["oid"]
    try:
        response=requests.get(ORDER_SERVICE+"/vieworder",json={"oid":oid})
        if response.status_code==200:
            data=response.json()
            print(data)
            isValid=data["success"]
            if isValid:
                return render_template("results.html",msg=data["data"])
            else:
                return render_template("results.html",msg=data["msg"])
    except Exception as e:
        return render_template("results.html",msg=str(e))

def viewUser(uName):
    return render_template("viewUser.html",uName=uName)

def main():
    app.run(debug=True,host="0.0.0.0",port=10000)

if __name__=='__main__':
    main()