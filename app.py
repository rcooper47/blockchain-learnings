#!/usr.bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from sqlhelpers import *
from forms import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'crypto'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)
@app.route("/register", methods = ["GET", "POST"])
def register():
	form = RegisterForm(request.form)
	users = Table("users", "name", "email", "username", "password")
	if request.method == 'POST' and form.validate():
		pass
	return render_template('register.html', form = form)



@app.route("/")
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.secret_key = 'secret123'
	app.run(debug = True)