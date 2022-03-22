from crypt import methods
from flask import Flask, redirect, render_template, session, flash, request
from web import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(69).hex()

#список домов:
@app.route('/')
def index():
    res = returnhomes()
    if res[0] == None:
        return render_template('index.html', homes=res)
    return render_template('index.html', homes=res[0])

@app.route('/auth', methods=['GET', 'POST'])
def authg():
    if session.get('user') == None:
        if request.method == "POST":
            acc = request.form.get('acc')
            key = request.form.get('key')
            email = request.form.get('email')
            number = request.form.get('number')
            res = auth(acc, key, email, number)
            if res[1] != None:
                return f"error: {res[1]}"
            session['user'] = res
            return redirect('/lk')
        else:
            return render_template('auth.html')
    else:
        return redirect('/')

@app.route('/reg', methods=['GET', 'POST'])
def reg1():
    if session.get('user') == None:
        if request.method == "POST":
            acc = request.form.get('acc')
            key = request.form.get('key')
            fio = request.form.get('fio').split(',')
            email = request.form.get('email')
            number = request.form.get('number')
            res = reg(acc, key, fio, email, number)
            if res[0] == False:
                return f"error: {res[1]}"
            return redirect('/auth')
        else:
            return render_template('reg.html')
    else:
        return redirect('/')

@app.route('/newhome', methods=['GET', 'POST'])
def newhome():
    if session.get('user') == None:
       if request.method == 'POST':
        res = addNewAdmin()
        if res[0] == None:
            return render_template('newhome.html', addadmin=res)
        return render_template('newhome.html', addadmin=res[0])
    return redirect('/auth')
    



@app.route('/home<home>')
def home(home):
    if session.get('user') == None:
        return redirect('/')
    return render_template('/home')


@app.route('/add', methods=['GET', 'POST'])
def adaddNewAdmin1():
    if session.get('admin') == None:
        if request.method == "POST":
            acc = request.form.get('acc')
            datareg = request.form.get('data')
            res = addNewAdmin(acc, datareg)
            if res[0] == False:
                return f"error: {res[1]}"
            return redirect('/auth')
        else:
            return render_template('add.html')
    else:
        return redirect('/')


if __name__ == "__main__":
    app.run(host=config["node2"]["ip"], port=80, debug=True)