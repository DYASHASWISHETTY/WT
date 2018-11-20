#-*- coding: utf-8 -*-
from flask import render_template
from flask import request,redirect,url_for
from app import app
import sys
import json
import quest
import psycopg2
import psycopg2.extras
from quest import parse
conn = psycopg2.connect("dbname='wt2' user='divya' host='localhost' password='divya'")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
@app.route('/')
@app.route('/signUp')
def signUp():
    return render_template('signUp.html', title='Next',user="")
@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user1 =  request.form['name']
    email1 = request.form['email']
    phone = request.form['phone']
    password1 = request.form['password']
    use=({"name":user1,"email":email1,"gender":"male","password1":password1,"phone":phone})
    try:
        cur.execute("""insert into Users(email,name,password,phone_no) values (%(email)s,%(name)s,%(password1)s,%(phone)s)""",use)
        return render_template('login.html', title='Next', user= "")
    except:
        return render_template('signUp.html', title='Next',user="Email already in use")
    return render_template('login.html', title='Next', user= "")
@app.route('/login', methods=['POST'])
def login():
    user =  request.form['username']
    password = request.form['password']
    users=({"username":user, "password":password})
    cur.execute("""SELECT * from users where name=%(username)s and password=%(password)s""",users)
    rows = cur.fetchall()
    if(rows):
        return render_template('home.html', title='Next', user=users)
    else:
	return render_template('login.html',title='Next',user="Invalid usermame and password")

@app.route('/index',methods = ['POST', 'GET'])
def sucess1():
    textinput =  request.form['fileToUpload']
    questions=parse(textinput)
    user = {"username":"divya" }
    return render_template('index.html', title='Next', user=user,questions=questions)
    #return json.dumps({'status':'OK','user':user});


@app.route('/index1', methods=['POST','GET'])
def success():
    print("---------------------",request)
    if(request.method == "POST"):
        print("all is weel")
        name=request.args.get('postVars')
        print(name)
    """
    users =  request.args['fileToUpload']
    file1=str(name)
    print("yakkappa-----------------\n")
    user = {"username": users }
    filehandle = open(file1, 'r')
    textinput = filehandle.read()
    questions=parse(textinput)
    #user = {'username': name}"""
    return render_template('index.html', title='Next', user="")
