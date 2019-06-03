'''File controller'''
import os
import psycopg2
from flask import Flask, redirect, url_for, render_template, request
import urllib.parse as urlparse
from flask_sqlalchemy import SQLAlchemy
from initDB import admin_table

app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def index():
	
	return render_template('admin-login.html')

@app.route('/admin_login',methods=['POST','GET'])
def admin_login():

	user_name=request.form['user_name']
	pass_word=request.form['pass_word']
	
	obj_admin_table=admin_table()
	login_string=obj_admin_table.adminLogin(user_name,pass_word)
	
	if(login_string.ADMIN_USER_NAME!=user_name):

		return render_template('admin-login.html')

	else if(login_string.ADMIN_USER_NAME==user_name):

		return render_template('home.html')

    


@app.route('/add_admin_control',methods=['POST','GET'])
def add_admin_control():

	adm_name=request.form['adm_name']
	adm_mobNo=request.form['adm_mobNo']
	adm_userName=request.form['adm_userName']
	adm_password=request.form['adm_password']
    
	verbose="Admin could not be Added"

	obj_myDB=myDB()

	verbose=obj_myDB.add_admin(adm_name,adm_mobNo,adm_userName,adm_password)

	return render_template('verbose-page.html', verbose)
	
@app.route('/add_user_control',methods=['POST'])
def add_user_control():

	name_of_user=request.form['name_of_user']
	mobile_number=request.form['mobile_number']
	email_address=request.form['email_address']
	car_number=request.form['car_number']
    
	verbose="User could not be Added"

	obj_myDB=myDB()

	verbose=obj_myDB.user_details(name_of_user,mobile_number,email_address,car_number)

	return render_template('verbose-page.html', verbose)
	
@app.route('/temp_password_control',methods=['POST'])
def temp_password_control():

	user_name=request.form['user_name']
	temp_password=request.form['temp_password']
	re_enter_password=request.form['re_enter_password']

	if(temp_password==re_enter_password):

		obj_myDB=myDB()

		verbose_string=""

		verbose_string=obj_myDB.update_temp_admin_password(user_name,temp_password)

		return render_template('verbose-page.html', verbose_string)

if __name__ == '__main__':
	app.run(debug = True)
