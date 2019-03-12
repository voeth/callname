#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request,escape
from random import randint
app = Flask(__name__)


@app.route('/')
def hello() -> 'html':
    "确定首页的框架、样式"
    title = '欢迎使用点名宝'
    return render_template('home.html',
                           the_title = title)

@app.route('/callname',methods = ['GET','POST']) 
def return_result()->'html':
    #代码放在这个位置，一开始使用get方式来访问/callname，就会立即触发request.form['times']，而此时用户还未有任何操作，所以会抛出keyerror异常
    #if request.form['times'] == 'am':
        #path = r'C:\Users\mr。lang\Desktop\callname\static\am.csv'
    #elif request.form['times'] == 'night':
       # path = r'C:\Users\mr。lang\Desktop\callname\static\night.csv'
   # with open(path,encoding='utf8') as file:
        #index = 0
        #students = {}
        #for n in file:
            #name = n.split(',')
            #index +=1
        #students[index] = name[1].strip('"\n')

    title = '抽奖环节'
    if request.method=='GET':
        return render_template("return_name.html",
                           the_title=title,)
    if request.method=='POST':
    # 对于获取表单请求的数据，应该放在使用post方法访问web，用户有操作产生了数据后再触发request.form['times']，否则会产生keyerror异常
        if request.form['times'] == 'am':
            path = r'C:\Users\mr。lang\Desktop\callname\static\am.csv'
        elif request.form['times'] == 'night':
            path = r'C:\Users\mr。lang\Desktop\callname\static\night.csv'
        with open(path,encoding='utf8') as file:
            line=index = 0
            students = {}
            for n in file:
                line +=1 # 隐藏无用信息
                if line>5:
                    name = n.split(',')
                    index +=1
                    students[index] = name[1].strip('"\n')
        students.pop(index) # 删除空值的键
        return render_template("return_name.html",
                   the_title=title,
                   the_students=students[randint(1,index)])
               

@app.route('/table',methods = ['GET','POST'])
def table()->'html':
    title=('学号','班级')
    pass
            
app.run(debug=True)

