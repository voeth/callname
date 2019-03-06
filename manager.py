#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request,escape
app = Flask(__name__)
@app.route('/')
def searh() -> 'html':
    "确定首页的框架、样式"
    title = '欢迎使用点名宝'
    return render_template('enter.html',
                           the_title = title)

@app.route('/result',methods = ['POST']) 
def return_result()->'html':
    return render_template("the_result.html",
                           the_title='学生信息',)
                          
    
            
app.run(debug=True)

