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
	
	verbose="Please Enter Username and Password"
	return render_template('admin-login.html',verbose=verbose)
	
@app.route('/payment-details-control',methods = ['POST', 'GET'])
def payment_details_control():

	dropDown1=request.form['dropDown1']
	mob_number=request.form['mob_number']
	userDetails=Users.query.filter_by(MOBILE_NUMBER=mob_number).first()
	voilationRecord=Violations.query.filter_by(CAR_NO=userDetails.CAR_NO).first()
	
	if(dropDown1=="payment"):
	
		return render_template('payment.html',voilationRecord)
		
	elif(dropDown1=="generate-pdf"):
	
		return render_template('generate-pdf.html',voilationRecord)
		

@app.route('/remove-admin',methods = ['POST', 'GET'])
def remove_admin():
	
	user_name=request.form['user_name']
	mob_number=request.form['mob_number']
	
	rmAdmin=Admins.query.filter_by(MOBILE_NUMBER=mob_number).first()
	if(rmAdmin.ADMIN_USER_NAME==user_name):
		
		verbose="Removed admin "+user_name
		db.session.delete(rmAdmin)
		db.session.commit()
		return render_template('verbose-page.html', verbose)
		
	else:
		verbose="Unable to remove Admin ",user_name
		return render_template('verbose-page.html', verbose)
		
@app.route('/remove-user',methods = ['POST', 'GET'])
def remove_user():
	
	mob_number=request.form['mob_number']
	email_address=request.form['email_address']
	
	rmUser=Users.query.filter_by(MOBILE_NUMBER=mob_number).first()
	if(rmAdmin.EMAIL_ID==email_address):
		
		verbose="Removed User "+user_name
		db.session.delete(rmUser)
		db.session.commit()
		return render_template('verbose-page.html', verbose)
		
	else:
		verbose="Unable to remove User "+user_name
		return render_template('verbose-page.html', verbose)
	
@app.route('/admin_login',methods=['POST','GET'])
def admin_login():

	username=request.form['user_name']
	password=request.form['pass_word']
	verbose=""

	
	adminsTest=Admins.query.filter_by(ADMIN_USER_NAME=username).first()
		
	if(adminsTest.ADMIN_USER_NAME!=username or adminsTest.ADMIN_PASSWORD!=password):
		
		verbose="Incorrect Username or Password, Please re-enter your Details!!!"
		return render_template('admin-login.html',verbose=verbose)

	elif(adminsTest.ADMIN_USER_NAME==username and adminsTest.ADMIN_PASSWORD==password and username=="root"):

		return render_template('root-home.html')
		
	elif(adminsTest.ADMIN_USER_NAME==username and adminsTest.ADMIN_PASSWORD==password):

		return render_template('home.html')

@app.route('/add_admin_control',methods=['POST','GET'])
def add_admin_control():

	adm_name=request.form['adm_name']
	adm_mobNo=request.form['adm_mobNo']
	adm_userName=request.form['adm_userName']
	adm_password=request.form['adm_password']
	
	#verbose="Admin could not be Added"
	
	#app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
	#db=SQLAlchemy(app)
	#maxAdm = Admins.query.order_by(Admins.ADM_NO.desc()).first()
	#setAdmNo=maxAdm.ADM_NO + 1
	#insertNew=Admins(setAdmNo,adm_name,adm_mobNo,adm_userName,adm_password)
	#db.session.add(insertNew)
	#db.session.commit()

	#verbose="User "+adm_name+" Added as New Admin"
	verbose=addAdmins(adm_name,adm_mobNo,adm_userName,adm_password)

	return render_template('verbose-page.html', verbose=verbose)
	
@app.route('/add-user-control',methods=['POST'])
def add_user_control():

	name_of_user=request.form['name_of_user']
	mobile_number=request.form['mobile_number']
	email_address=request.form['email_address']
	state_code=request.form['state_code']
	number_code=request.form['number_code']
	area_code=request.form['area_code']
	pin=request.form['pin']
    
	car_number=state_code+"-"+number_code+"-"+area_code+"-"+pin
	
	verbose="User could not be Added"

	db=SQLAlchemy(app)
	maxUsr = Users.query.order_by(Admins.ADM_NO.desc()).first()
	setUsrNo=maxUsr.USR_NO + 1
	insertNew=Users(setUsrNo,adm_name,adm_mobNo,adm_userName,adm_password)
	db.session.add(insertNew)
	db.session.commit()
	
	verbose="User "+name_of_user+" Added"

	return render_template('verbose-page.html', verbose)
	
@app.route('/update-admin',methods=['POST'])
def update_admin():

	dropDown1=request.form['dropDown1']
	mob_number=request.form['mob_number']
	admin_name=request.form['admin_name']
	
	admDetails=Admins.query.filter_by(MOBILE_NUMBER=mob_number).first()
	
	if(dropDown1=="name"):
		
		admDetails.ADMIN_NAME=admin_name
		db.session.commit()
	
	elif(dropDown1=="mob_number"):
		
		admDetails.MOBILE_NUMBER=admin_name
		db.session.commit()
		
	elif(dropDown1=="user_name"):
		
		admDetails.ADMIN_USER_NAME=admin_name
		db.session.commit()
		
@app.route('/update-user',methods=['POST'])
def update_user():

	dropDown1=request.form['dropDown1']
	mob_number=request.form['mob_number']
	usr_name=request.form['usr_name']
	state_code=request.form['state_code']
	number_code=request.form['number_code']
	area_code=request.form['area_code']
	pin=request.form['pin']
	
	
	userDetails=Users.query.filter_by(MOBILE_NUMBER=mob_number).first()
	
	if(dropDown1=="name"):
		
		userDetails.NAME_OF_USER=usr_name
		db.session.commit()
	
	elif(dropDown1=="mob_number"):
		
		userDetails.MOBILE_NUMBER=usr_name
		db.session.commit()
		
	elif(dropDown1=="email_address"):
		
		userDetails.ADMIN_USER_NAME=usr_name
		db.session.commit()
		
	elif(dropDown1=="car_number"):
		
		car_no=state_code+"-"+number_code+"-"+area_code+"-"+pin
		userDetails.CAR_NO=car_no
		db.session.commit()
	
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
	
@app.route('/route-returnHome',methods=['POST','GET'])
def route_returnHome():
	
	return render_template('generate-pdf.html')
	
class Admins(db.Model):

	ADM_NO=db.Column(db.Integer,primary_key=True)
	ADMIN_NAME=db.Column(db.String(20),unique=False)
	MOBILE_NUMBER=db.Column(db.BigInteger,unique=True)
	ADMIN_USER_NAME=db.Column(db.String(10),unique=True)
	ADMIN_PASSWORD=db.Column(db.String(16),unique=False)
	
	def __init__(self,ADM_NO,ADMIN_NAME,MOBILE_NUMBER,ADMIN_USER_NAME,ADMIN_PASSWORD):
		
		self.ADM_NO=ADM_NO
		self.ADMIN_NAME=ADMIN_NAME
		self.MOBILE_NUMBER=MOBILE_NUMBER
		self.ADMIN_USER_NAME=ADMIN_USER_NAME
		self.ADMIN_PASSWORD=ADMIN_PASSWORD
		
		
class Users(db.Model):

	USR_NO=db.Column(db.Integer,primary_key=True)
	NAME_OF_USER=db.Column(db.String(20),unique=False)
	MOBILE_NUMBER=db.Column(db.BigInteger,unique=True)
	EMAIL_ID=db.Column(db.String(30),unique=True)
	CAR_NO=db.Column(db.String(13),unique=False)
	
	def __init__(self,USR_NO,NAME_OF_USER,MOBILE_NUMBER,EMAIL_ID,CAR_NO):
		
		self.USR_NO=USR_NO
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
	verbose="New Admin "+adm_name+" Added" 
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
	'''insertAdm=Admins(1,'MAIN_ADMIN',12345789,'root','ROOT1234')
	db.session.add(insertAdm)
	db.session.commit()
	insertUsr=Users(1,"User1",987654321,"testuser123@gmail.com","MH-01-CH-0007")
	db.session.add(insertUsr)
	db.session.commit()'''
	addAdmins('MAIN_ADMIN',12345789,'root','ROOT1234')
	addUsers("User1",987654321,"testuser123@gmail.com","MH-01-CH-0007")
