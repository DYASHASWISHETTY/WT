#-*- coding: utf-8 -*-
from flask import render_template
from flask import request,redirect,url_for
from app import app
import sys
import json
import quest
import psycopg2
from quest import parse
conn = psycopg2.connect("dbname='wt2' user='divya' host='localhost' password='divya'")
cur = conn.cursor()
@app.route('/')
@app.route('/signUp')
def signUp():
    cur.execute("""SELECT * from Users""")
    return render_template('signUp.html')
@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username']
    users={'username':user}
    password = request.form['password']
    return render_template('index.html', title='Next', user=users)
@app.route('/index',methods = ['POST', 'GET'])
def signUser():
    user =  request.form['username']
    return json.dumps({'status':'OK','user':user});
@app.route('/success/<name>', methods=['POST','GET'])
def success(name):
    file1=str(name)
    filehandle = open(file1, 'r')
    textinput = filehandle.read()
    questions=parse(textinput)
    user = {'username': name}
    return render_template('index.html', title='Next', user=user,questions=questions)
@app.route('/success1/<textinput>', methods=['POST','GET'])
def success1(textinput):
    questions=parse(textinput)
    user = {'username': "divya"}
    return render_template('index.html', title='Next', user=user,questions=questions)

      
