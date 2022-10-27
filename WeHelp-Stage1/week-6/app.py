from flask import Flask 
from flask import request 
from flask import redirect 
from flask import render_template 
from flask import session 
import mysql.connector

mydb = mysql.connector.connect(user='root', password='********',
                              host='localhost',
                              database='member') #資料庫連線
mycursor = mydb.cursor()     

app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/") #建立 Application 物件
app.secret_key="any string but secret" #設定 Session 的密鑰

@app.route("/")
def index():
    return render_template("index.html") #渲染首頁

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    name = str(name)
    username = request.form["username"]
    username = str(username)
    password = request.form["password"]
    password = str(password)
    if(name =="" or username == "" or password == ""): #驗證失敗
        return redirect('/error?message=請輸入帳號、密碼') #導向/error   
    mycursor.execute("SELECT username FROM member_list WHERE username='"+username+"'") #SQL指令 檢查是否有重複的帳號 (username)
    myresult = mycursor.fetchall()
    x=""
    for x in myresult:
        print(x)
    if (x != ""):#註冊失敗
        return redirect('/error?message=帳號已經被註冊') #導向/error
    else:#註冊成功
        session["name"]=name
        login = "已註冊"
        session["login"]=login   
        sql = "INSERT INTO member_list (name, username, password) VALUES (%s, %s, %s)" #SQL指令 新增資料
        val = (name, username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "新帳號註冊") 
        return redirect("/") #導向首頁


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    username = str(username)
    password = request.form["password"]
    password = str(password)
    if(username == "" or password == ""): #驗證失敗
        return redirect('/error?message=請輸入帳號、密碼') #導向/error
    mycursor.execute("SELECT * FROM member_list WHERE username='"+username+"' and password='"+password+"'") #SQL指令 是否有對應的帳號、密碼
    myresult = mycursor.fetchall()
    x=""
    for x in myresult:
        print(x)
    if (x == ""):#驗證失敗
        return redirect('/error?message=帳號或密碼輸入錯誤') #導向/error
    else: #驗證成功
        session["id"]=x[0] #使用者編號
        session["name"]=x[1] #姓名
        login = "已登入"
        session["login"]=login     
        return redirect("/member") #導向/member

@app.route("/error", methods=["GET"])
def error():
    message = request.args.get("message","")
    return render_template("error.html", message=str(message)) #渲染失敗頁面  

@app.route("/member")
def member():
    name = session["name"]
    login = session["login"]
    if(login == "已註冊"):
        mycursor.execute("SELECT member_list.name, message_list.content FROM member_list INNER JOIN message_list ON message_list.member_id=member_list.id ORDER BY message_list.time DESC;") #SQL指令 向資料庫取得所有留言內容
        myresult = mycursor.fetchall()
        x=""
        current_username_array=[]
        current_content_array=[]
        for x in myresult:
         username = x[0]+":"
         content = x[1]
         current_username_array.append(username)
         current_content_array.append(content)
        return render_template("member.html", name=str(name), content=str(x)) #渲染會員頁
    elif(login != "已登入"):
        return redirect("/") #導向首頁    
    else:
        mycursor.execute("SELECT member_list.name, message_list.content FROM member_list INNER JOIN message_list ON message_list.member_id=member_list.id ORDER BY message_list.time DESC;") #SQL指令 向資料庫取得所有留言內容
        myresult = mycursor.fetchall()
        x=""
        current_username_array=[]
        current_content_array=[]
        for x in myresult:
         username = x[0]+":"
         content = x[1]
         current_username_array.append(username)
         current_content_array.append(content)
        return render_template("member.html", name=str(name), username=current_username_array, content=current_content_array) #渲染會員頁

@app.route("/signout")
def signout():
    login = "未登入"
    session["login"]=login
    userid = ""
    session["id"]=userid #清空 使用者編號
    username = ""
    session["name"]=username #清空 姓名
    return redirect("/") #導向首頁
    
@app.route("/message", methods=["POST"])
def message():
    content = request.form["content"]
    content = str(content)
    if(content == ""): #留言失敗
        return redirect('/error?message=請輸入內容') #導向/error
    userid=session["id"]
    sql = "INSERT INTO message_list (member_id, content) VALUES (%s, %s)" #SQL指令 將留言內容紀錄到 message 資料表
    val = (userid, content)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "新留言內容") 
    return redirect("/member") #導向會員頁

app.run(port=3000)


