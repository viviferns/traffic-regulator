'''File controller'''
import os
import psycopg2
from flask import Flask, redirect, url_for, render_template, request
import urllib.parse as urlparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
db=SQLAlchemy(app)


@app.route('/',methods = ['POST', 'GET'])
def index():
	
	return render_template('admin-login.html')

@app.route('/admin_login',methods=['POST','GET'])
def admin_login():

	username=request.form['user_name']
	password=request.form['pass_word']
	authentication=True
	
	adminsTest=Admins.query.filter_by(ADMIN_USER_NAME=username).first()
		
	if(adminsTest.ADMIN_USER_NAME!=username and adminsTest.ADMIN_PASSWORD!=password):

		return render_template('admin-login.html')

	elif(adminsTest.ADMIN_USER_NAME==username and adminsTest.ADMIN_PASSWORD==password and username=="root"):

		return render_template('root-home.html',authentication=authentication)
		
	elif(adminsTest.ADMIN_USER_NAME==username and adminsTest.ADMIN_PASSWORD==password):

		return render_template('home.html',authentication=authentication)

@app.route('/add_admin_control',methods=['POST','GET'])
def add_admin_control():

	adm_name=request.form['adm_name']
	adm_mobNo=request.form['adm_mobNo']
	adm_userName=request.form['adm_userName']
	adm_password=request.form['adm_password']
    
	verbose="Admin could not be Added"

	verbose=addAdmins(adm_name,adm_mobNo,adm_userName,adm_password)

	return render_template('verbose-page.html', verbose)
	
@app.route('/add_user_control',methods=['POST'])
def add_user_control():

	name_of_user=request.form['name_of_user']
	mobile_number=request.form['mobile_number']
	email_address=request.form['email_address']
	car_number=request.form['car_number']
    
	verbose="User could not be Added"

	obj_myDB=myDB()

	verbose=addUsers(name_of_user,mobile_number,email_address,car_number)

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
		
@app.route('/route-addAdmin',methods=['POST','GET'])
def route_addAdmin():
	
	return render_template('addAdmin.html')
	
@app.route('/route-updateAdminPassword',methods=['POST','GET'])
def route_updateAdminPassword():
	
	return render_template('updateAdmin.html')
	
@app.route('/route-removeAdmin',methods=['POST','GET'])
def route_removeAdmin():
	
	return render_template('removeAdmins.html')
	
@app.route('/route-addUser',methods=['POST','GET'])
def route_addUser():
	
	return render_template('addUser.html')
	
@app.route('/route-updateUser',methods=['POST','GET'])
def route_updateUser():
	
	return render_template('updateUser.html')
	
@app.route('/route-removeUser',methods=['POST','GET'])
def route_removeUser():
	
	return render_template('removeUser.html')
	
@app.route('/route-fetchUserDetails',methods=['POST','GET'])
def route_fetchUserDetails():
	
	return render_template('payment.html')
	
@app.route('/route-payment',methods=['POST','GET'])
def route_payment():
	
	return render_template('payment-details.html')
	
@app.route('/route-generate-pdf',methods=['POST','GET'])
def route_generate_pdf():
	
	return render_template('generate-pdf.html')
	
		
class Admins(db.Model):

	ADM_NO=db.Column(db.Integer,primary_key=True)
	ADMIN_NAME=db.Column(db.String(20),unique=False)
	MOBILE_NUMBER=db.Column(db.Integer,unique=True)
	ADMIN_USER_NAME=db.Column(db.String(10),unique=True)
	ADMIN_PASSWORD=db.Column(db.String(16),unique=False)
	
	def __init__(self,ADM_NO,ADMIN_NAME,MOBILE_NUMBER,ADMIN_USER_NAME,ADMIN_PASSWORD):
		
		self.ADMIN_NAME=ADMIN_NAME
		self.MOBILE_NUMBER=MOBILE_NUMBER
		self.ADMIN_USER_NAME=ADMIN_USER_NAME
		self.ADMIN_PASSWORD=ADMIN_PASSWORD
		
		
class Users(db.Model):

	USR_NO=db.Column(db.Integer,primary_key=True)
	NAME_OF_USER=db.Column(db.String(20),unique=False)
	MOBILE_NUMBER=db.Column(db.Integer,unique=True)
	EMAIL_ID=db.Column(db.String(30),unique=True)
	CAR_NO=db.Column(db.String(10),unique=False)
	
	def __init__(self,USR_NO,NAME_OF_USER,MOBILE_NUMBER,EMAIL_ID,CAR_NO):
		
		self.NAME_OF_USER=NAME_OF_USER
		self.MOBILE_NUMBER=MOBILE_NUMBER
		self.EMAIL_ID=EMAIL_ID
		self.CAR_NO=CAR_NO
		
class Locations(db.Model):

	LOC_NO=db.Column(db.Integer,primary_key=True)
	LOC_NAME=db.Column(db.String(20),unique=True)
	
	def __init__(self,LOC_NO,LOC_NAME,MOBILE_NUMBER,EMAIL_ID,CAR_NO):
		
		self.LOC_NAME=LOC_NAME
		
class Violations(db.Model):

	REC_NO=db.Column(db.Integer,primary_key=True)
	TIME_STAMP=db.Column(db.Integer,unique=False)
	CAR_NO=db.Column(db.String(30),unique=True)
	LOC_NAME=db.Column(db.String(30),unique=True)
	FINE_AMOUNT=db.Column(db.Integer,unique=False)
	
	def __init__(self,REC_NO,TIME_STAMP,CAR_NO,LOC_NAME,VIOLATION_IMAGE,FINE_AMOUNT):
		
		self.TIME_STAMP=TIME_STAMP
		self.CAR_NO=CAR_NO
		self.LOC_NAME=LOC_NAME
		self.VIOLATION_IMAGE=VIOLATION_IMAGE
		self.FINE_AMOUNT=FINE_AMOUNT
		

def adminLogin(username,password):
	
	adminsTest=Admins.query.filter_by(ADMIN_USER_NAME=username).first()
	return adminsTest
		
def addAdmins(adm_name,adm_mobNo,adm_userName,adm_password):

	insert=Admins(adm_name,adm_mobNo,adm_userName,adm_password)
	db.session.add(insert)
	db.session.commit()
	verbose="New Admin Added"
	return verbose
	
def addUsers(name_of_user,mobile_number,email_address,car_number):
	
	insert=Users(adm_name,adm_mobNo,adm_userName,adm_password)
	db.session.add(insert)
	db.session.commit()
	verbose="New User Added"
	return verbose
	

if __name__ == '__main__':
	#app.run(debug = True)
	db.create_all()
	insert=Admins(1,'MAIN_ADMIN',123456789,'root','ROOT1234')
	db.session.add(insert)
	db.session.commit()
