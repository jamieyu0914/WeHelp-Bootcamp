from crypt import methods
from email import message
import logging
from urllib.request import Request
from flask import Flask # 載入 
from flask import request # 載入 request 物件
from flask import redirect # 載入 redirect 函式
from flask import render_template # 載入 render_template 函式
from flask import session
import json

app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/") #建立 Application 物件
app.secret_key="any string but secret" #設定 Session 的密鑰

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST","GET"])
def sign():
    username = request.form["name"]
    username = str(username)
    userpassword = request.form["password"]
    userpassword = str(userpassword)
    if(username == ""):
        message="請輸入帳號、密碼"
        session["message"]=message
        return render_template("error.html", message=message) 
    elif(userpassword == ""):
        message="請輸入帳號、密碼"
        session["message"]=message
        return  render_template("error.html", message=message) 
    elif(username != "test"):
        message="帳號、或密碼輸入錯誤"
        session["message"]=message
        return  render_template("error.html", message=message) 
    elif(userpassword != "test"):
        message="帳號、或密碼輸入錯誤"
        session["message"]=message
        return  render_template("error.html", message=message) 
    else:
        login = "已登入"
        session["login"]=login      
        return render_template("member.html") 

@app.route("/error")
def error():
    message = request.args.get("message","")
    return render_template("error.html", message=message)   

@app.route("/member")
def member():
    login = session["login"]
    if(login != "已登入" ):
        return render_template("index.html")   

@app.route("/signout")
def signout():
    login = "已登出"
    session["login"]=login      
    return render_template("index.html")

@app.route("/calculate", methods=["GET"])
def calculate():
    Number = request.args.get("integer","")
    Number = str(Number)
    if(Number==""):
        result="請輸入正整數"
        return render_template("result.html", data=str(result))    
    result=0
    for n in range(1, int(Number)+1):
        result=n*n
    return render_template("result.html", data=str(result))    










app.run(port=3000)


