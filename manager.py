#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request,escape
from random import randint
app = Flask(__name__)

with open(r'C:\Users\mr。lang\Desktop\callname\static\pm_classmates.csv',encoding='utf8') as pm:
    index = 0
    students = {}
    for n in pm:
        name = n.split(',')
        index +=1
        students[index] = name[2].strip('"\n')
@app.route('/')
def searh() -> 'html':
    "确定首页的框架、样式"
    title = '欢迎使用点名宝'
    return render_template('home.html',
                           the_title = title)

@app.route('/callname',methods = ['GET','POST']) 
def return_result()->'html':
    global students,index
    if request.method=='GET':
        return render_template("return_name.html",
                           the_title='抽奖环节',)
    if request.method=='POST':
        global students,index
        return render_template("return_name.html",
                   the_title='抽奖环节',
                   the_students=students[randint(1,index)])
                          
    
            
app.run(debug=True)

