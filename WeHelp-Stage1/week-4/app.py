from flask import Flask # 載入 Flask
from flask import request # 載入 request 物件
from flask import redirect # 載入 redirect 函式
from flask import render_template # 載入 render_template 函式
from flask import session # 載入 session

app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/") #建立 Application 物件
app.secret_key="any string but secret" #設定 Session 的密鑰

@app.route("/")
def index():
    return render_template("index.html") #渲染首頁

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["name"]
    username = str(username)
    userpassword = request.form["password"]
    userpassword = str(userpassword)
    if(username == "" or userpassword == ""): #驗證失敗
        return redirect('/error?message=請輸入帳號、密碼') #轉至/error
    elif(username != "test" or userpassword != "test"):
        return  redirect('/error?message=帳號、或密碼輸入錯誤') #轉至/error
    else: #驗證成功
        login = "已登入"
        session["login"]=login     
        return redirect("/member") #轉至/member

@app.route("/error", methods=["GET"])
def error():
    message = request.args.get("message","")
    return render_template("error.html", message=str(message)) #渲染失敗頁面  

@app.route("/member")
def member():
    login = session["login"]
    if(login != "已登入" ):
        return redirect("/") #導向首頁
    else:
        return render_template("member.html") #渲染會員頁

@app.route("/signout")
def signout():
    login = "未登入"
    session["login"]=login      
    return redirect("/") #導向首頁

@app.route('/square/', methods=["GET"]) 
def square():
    Number = request.args.get("integer","")
    Number = str(Number)
    if (Number==""): 
        return render_template("square.html", integer="請輸入正整數") #欄位未輸入 渲染結果頁    
    return redirect(f"/square/{Number}") #轉至/square/<integer>
    


@app.route("/square/<integer>", methods=["GET"])
def caculate(integer=None):
        Number = request.args.get("integer","")
        Number = str(Number)
        if(Number==""):
            Numbers = str(integer)
            if(Numbers=='None'):
                return render_template("square.html", integer="請輸入正整數") #網址未輸入 渲染結果頁       
            elif(Numbers!=""): 
                result=0
                for n in range(1, int(mbers)+1):
                    result=n*n #計算平方 n**2
                return render_template("square.html", integer=str(result)) #網址輸入 渲染結果頁  
        result=0;   
        for n in range(1, int(Number)+1):
            result=n*n #計算平方 n**2
        return render_template("square.html", integer=str(result)) #欄位輸入 渲染結果頁
    


app.run(port=3000)

