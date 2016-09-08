#_*_coding:utf-8_*_
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('MVC_Home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('MVC_Signin.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form('username')
    password = request.form('password')
    if username == 'admin' and password == 'password':
        return render_template('MVC_Signin.html', username=username)
    return render_template('form.htnl', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
# Flask by render_template fun to 实现 model 渲染 like Web 框架
