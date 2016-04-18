# coding:utf-8
import sqlite3
import config
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash


# create little application
app = Flask(__name__)
app.config.from_pyfile('../config.py')


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def index_main():
    return 'aloha'
    
     
@app.route('/post/<pid>')
def get_post(pid):
    pass

  
if __name__ == '__main__':
    app.run(debug=True,port=4000)