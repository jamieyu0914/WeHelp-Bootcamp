from flask import Flask 
from flask import request 
from flask import Response
from flask import redirect 
from flask import render_template 
from flask import session
from flask import jsonify
from mysql.connector import Error
from mysql.connector import pooling
import json


connection_pool = pooling.MySQLConnectionPool(pool_name="my_connection_pool",
                                                pool_size=5,
                                                pool_reset_session=True,
                                                host='localhost',
                                                database='member',
                                                user='root',
                                                password='m6ao3ao3')



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
    username = request.form["username"]
    password = request.form["password"]
    if(name =="" or username == "" or password == ""): #驗證失敗
        return redirect('/error?message=請輸入帳號、密碼') #導向/error 
    sql = "SELECT username FROM member_list WHERE username=%s" #SQL指令 檢查是否有重複的帳號 (username)
    val = (username,)
    try:
        # Get connection object from a pool
        connection_object = connection_pool.get_connection() #連線物件 commit時 需要使用
        cursor = connection_object.cursor()
        print("MySQL connection is opened")
        cursor.execute(sql, val)
        myresult = cursor.fetchall()
        x=""
        for x in myresult:
            print(x)
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)
    finally:
        # closing database connection.    
        cursor.close()
        connection_object.close()
    print("MySQL connection is closed")       
    if (x != ""):#註冊失敗
        return redirect('/error?message=帳號已經被註冊') #導向/error
    else:#註冊成功
        session["name"]=name
        login = "已註冊"
        session["login"]=login   
        sql = "INSERT INTO member_list (name, username, password) VALUES (%s, %s, %s)" #SQL指令 新增資料
        val = (name, username, password)
        try:
            # Get connection object from a pool
            connection_object = connection_pool.get_connection() #連線物件 commit時 需要使用
            cursor = connection_object.cursor()
            print("MySQL connection is opened")
            cursor.execute(sql, val)
            connection_object.commit()
        except Error as e:
            print("Error while connecting to MySQL using Connection pool ", e)
        finally:
            # closing database connection.    
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")            
            print("新帳號註冊") 
        return redirect("/") #導向首頁

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if(username == "" or password == ""): #驗證失敗
        return redirect('/error?message=請輸入帳號、密碼') #導向/error
    sql = "SELECT * FROM member_list WHERE username=%s and password=%s" #SQL指令 是否有對應的帳號、密碼
    val = (username, password)
    try:
        # Get connection object from a pool
        connection_object = connection_pool.get_connection() #連線物件 commit時 需要使用
        cursor = connection_object.cursor()
        print("MySQL connection is opened")
        cursor.execute(sql, val) 
        myresult = cursor.fetchall()
        x=""
        for x in myresult:
            print(x)
    except Error as e:
            print("Error while connecting to MySQL using Connection pool ", e)
    finally:
        # closing database connection.    
        cursor.close()
        connection_object.close()
        print("MySQL connection is closed")           
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
    return render_template("error.html", message=message) #渲染失敗頁面  

@app.route("/member")
def member():
    name = session["name"]
    login = session["login"]
    if(login != "已登入"):
        return redirect("/") #導向首頁    
    else:
        return render_template("member.html", name=name) #渲染會員頁

@app.route("/api/member", methods=["GET"])
def apimember():
    username = request.args.get("username","")
    login = session["login"]
    if(username == ""):
        return jsonify({"data":None})

    if(login != "已登入"):
        return redirect("/") #導向首頁    
    else:
        sql = "SELECT * FROM member_list WHERE username=%s" #SQL指令 是否有對應的帳號、密碼
        val = (username,)
        try:
            # Get connection object from a pool
            connection_object = connection_pool.get_connection() #連線物件 commit時 需要使用
            cursor = connection_object.cursor()
            print("MySQL connection is opened")
            cursor.execute(sql,val)
            myresult = cursor.fetchall()
            x=""
            for x in myresult:
                userid = x[0]
                name = x[1]
                username = x[2]    
            print(name)
        except Error as e:
            print("Error while connecting to MySQL using Connection pool ", e)
        finally:
            # closing database connection.    
            cursor.close()
            connection_object.close()
        print("MySQL connection is closed")     
        return jsonify({
                "data":{
                    "id":userid,
                    "name":name,
                    "username":username
                    }
                }     )

@app.route('/api/member', methods=['PATCH'])
def patchmember():
    if request.method == "PATCH":
        login = session["login"]
        userid = session["id"]
        patch = request.get_json()
        username = patch["name"]
        print(username)
        
        if(login != "已登入" or username == ""):
            return jsonify({"error":True})
        else:
            sql = "UPDATE member_list  SET name = %s WHERE id = %s" #SQL指令 更新對應的姓名欄位
            val = (username, userid )
            try:
                # Get connection object from a pool
                connection_object = connection_pool.get_connection() #連線物件 commit時 需要使用
                cursor = connection_object.cursor()
                print("MySQL connection is opened")
                cursor.execute(sql,val)
                connection_object.commit()
                session["username"] = username
            except Error as e:
                print("Error while connecting to MySQL using Connection pool ", e)
                return jsonify({"error":True})
            finally:
                # closing database connection.    
                cursor.close()
                connection_object.close()
            print("MySQL connection is closed")
            return jsonify({"ok":True})       

@app.route("/signout")
def signout():
    login = "未登入"
    session["login"]=login
    userid = ""
    session["id"]=userid #清空 使用者編號
    username = ""
    session["name"]=username #清空 姓名
    return redirect("/") #導向首頁

app.run(port=3000)





