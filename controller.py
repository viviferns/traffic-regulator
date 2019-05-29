'''File controller'''
import os
import psycopg2
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
	
	#DATABASE_URL=os.environ['DATABASE_URL']
	
	db_url="postgres://bjjsheknydiasx:12ed7523f49dd98a0e7ab7877a50e68fcab3e1899f5eb9fe06d9e7d55a172c44@ec2-54-225-95-183.compute-1.amazonaws.com:5432/dfcuab4bf4j09"

	# Open database connection
	conn=psycopg2.connect(db_url,sslmode='require')
	
	print(db_url)

	# Prepare a cursor object
	cursor = conn.cursor()
	
	query="select count(ADMIN_USER_NAME) from admin_table"
		
	result=0
		
	try:
		
		cursor=initiateDB.connect_database()

		# Execute SQL query using execute() method.
		cursor.execute(query)

		# Fetch result
		result=cursor.fetchall()
			
		cursor.close()

	except:
            
		return "Error while fetching record"
	
	if(result>0):
		
		return render_template('admin-login.html')
			
	else:		

		query1="CREATE TABLE user_table(USR_NO SERIAL PRIMARY KEY NOT NULL, NAME_OF_USER VARCHAR(30) NOT NULL, MOBILE_NUMBER NUMBER NOT NULL, EMAIL_ID VARCHAR(30) NOT NULL, CAR_NO VARCHAR(10) NOT NULL)"

		query2="CREATE TABLE admin_table(ADM_NO SERIAL PRIMARY KEY NOT NULL, ADMIN_NAME VARCHAR(30) NOT NULL, MOBILE_NUMBER NUMBER NOT NULL,ADMIN_USER_NAME VARCHAR(20) NOT NULL, ADMIN_PASSWORD VARCHAR(16) NOT NULL)"

		query3="INSERT INTO  admin_table VALUES(1,'MAIN_ADMIN',123456789,'root','ROOT1234')"

		query4="CREATE TABLE locations (LOC_NO SERIAL PRIMARY KEY NOT NULL,LOC_NAME VARCHAR(10) NOT NULL)"

		query5="CREATE TABLE violation_record(REC_NO SERIAL PRIMARY KEY NOT NULL, TIME_STAMP TIMESTAMP NOT NULL,CAR_NO VARCHAR(10) NOT NULL,LOC_NAME VARCHAR(10) NOT NULL,VIOLATION_IMAGE BLOB NOT NULL,FINE_AMOUNT VARCHAR(30) NOT NULL)"

		try:

			# Execute SQL query using execute() method.
			cursor.execute(query1)

			cursor.execute(query2)

			cursor.execute(query4)
			
			cursor.execute(query5)


			# Commit your changes in the database
			cursor.commit()
			
			cursor.execute(query3)
			
			cursor.commit()
			
			cursor.close()
			
			return render_template('admin-login.html')

		except:

			# Rollback in case there is any error
			cursor.rollback()
			
			cursor.close()

@app.route('/admin_login',methods=['POST','GET'])
def admin_login():

	user_name=request.form['user_name']
	pass_word=request.form['pass_word']

	obj_myDB=myDB()

	login_string=obj_myDB.admin_login(user_name,pass_word)

	if(login_string!="SUCCESSFUL"):

		return render_template('admin-login.html')

	else:

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
