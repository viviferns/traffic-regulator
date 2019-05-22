import os
import psycopg2

class myDB:

'''    user_name, pass_word, database_name,result=None

    def set_database(user_name, pass_word, database_name):
        
        myDB.user_name=user_name
        myDB.pass_word=pass_word
        myDB.database_name=database_name
'''
		
	def connect_database():
	
		DATABASE_URL=os.environ['DATABASE_URL']

		# Open database connection
		conn=psycopg2.connect(DATABASE_URL,sslmode='require')

		# Prepare a cursor object
		cursor = conn.cursor()

		return cursor
        

	def add_location(location):

		cursor=myDB.connect_database()

		query="INSERT INTO locations VALUES(",location,")"
		
		try:

			# Execute SQL query using execute() method.
			cursor.execute(query)

			# Commit your changes in the database
			cursor.commit()

		except:

			# Rollback in case there is any error
			cursor.rollback()

	def add_violation_record(time_stamp,car_number,location,vio_image):

		cursor=myDB.connect_database()

		query="insert into violation_record VALUES(",time_stamp,",",car_number,",",location,",",vio_image,",","1000",")"

		try:

			# Execute SQL query using execute() method.
			cursor.execute(query)

			# Commit your changes in the database
			cursor.commit()

		except:

			# Rollback in case there is any error
			cursor.rollback()

	def update_violation_record(time_stamp):

		cursor=myDB.connect_database()

		query="DELETE FROM violation_record WHERE AND TIME_STAMP=",time_stamp

		return_statement=""

	try:

		# Execute SQL query using execute() method.
		cursor.execute(query)

		# Commit your changes in the database
		cursor.commit()

		return_statement="Payment Received"

	except:

		# Rollback in case there is any error
		cursor.rollback()

		return_statement="Could not collect Payment"

        return return_statement

	def user_details(name_of_user,mobile_number,email_address,car_number):
        
		cursor=myDB.connect_database()

		query1="select count(car_number) from user_table WHERE CAR_NO=",car_number," and EMAIL_ID=",email_address

		query2="insert into user_table values(",name_of_user,",",mobile_number,",",email_address,",",car_number,")"

		verbose=""

		try:

			# Execute SQL query using execute() method.
			if(cursor.execute(query1)>0):
                
				cursor.execute(query2)

				cursor.commit()

				verbose="New User ",name_of_user," Added"

				return verbose

			else:

				verbose="User already exists"

                		return verbose

		except:

			# Rollback in case there is any error
			cursor.rollback()

			verbose="Error Unknown"

			return verbose

	def add_admin(adm_name,adm_mobNo,adm_userName,adm_password):

		cursor=myDB.connect_database()

		query1="select count(ADMIN_USER_NAME) from admin_table WHERE ADMIN_USER_NAME=",adm_userName," and MOBILE_NUMBER=",adm_mobNo

		query2="INSERT INTO admin_table VALUES(",adm_name,",",adm_mobNo,",",adm_userName,",",adm_password,")"

		verbose=""

		try:

			# Execute SQL query using execute() method.
			if(cursor.execute(query1)>0):
                
				cursor.execute(query2)

				cursor.commit()

				verbose="New Admin Added, please ask ", adm_name, " to Login and change his Login Password Immediately"

			else:

				verbose="Admin already exists"

		except:

			# Rollback in case there is any error
			cursor.rollback()
            
	def fetch_record(mob_number):

		cursor=myDB.connect_database()

		query="select v.TIME_STAMP,v.CAR_NO,v.LOC_NAME,v.FINE_AMOUNT,v.VIOLATION_IMAGE,u.EMAIL_ID from violation_record v INNER JOIN user_table u ON v.CAR_NO=u.CAR_NO and u.MOBILE_NUMBER=",mob_number

		try:

			# Execute SQL query using execute() method.
			cursor.execute(query)

			# Fetch result
			result=cursor.fetchall()

			return result

		except:
            
			return "Error while fetching record"


	def update_admin_password(user_name,old_pass_word,new_pass_word):

		cursor=myDB.connect_database()

		query="UPDATE admin_table SET ADMIN_PASSWORD=",new_pass_word," WHERE ADMIN_USER_NAME LIKE ",user_name

		try:

			# Execute SQL query using execute() method.
			cursor.execute(query)

			# Commit your changes in the database
			cursor.commit()

		except:

			# Rollback in case there is any error
			cursor.rollback()

	def update_temp_admin_password(user_name,temp_password):

		cursor=myDB.connect_database()

		verbose=""

		query="UPDATE admin_table SET ADMIN_PASSWORD=",temp_password," WHERE ADMIN_USER_NAME LIKE ",user_name

		try:

			# Execute SQL query using execute() method.
			cursor.execute(query)

			# Commit your changes in the database
			cursor.commit()

			verbose="Password Updated, please ask ", user_name ," to update his password Immediately!!!"

		except:

			# Rollback in case there is any error
			cursor.rollback()

			verbose="Password cannot be updated right now, please try later."

			return verbose


	def admin_login(user_name,pass_word):

		cursor=myDB.connect_database()

		query="select count(ADMIN_USER_NAME) from admin_table WHERE ADMIN_USER_NAME=",user_name," and ADMIN_PASSWORD=",pass_word

		login_string=""

		try:

			# Execute SQL query using execute() method.
			cursor.execute(query)

			# Fetch result
			result=cursor.fetchall()

		except:
            
			return "Error while fetching record"
        
		if(result==1):

			login_string="SUCCESSFUL"

		else:

			login_string="FAILED"

        

		return login_string
