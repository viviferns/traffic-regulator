import os
import psycopg2

class initiateDB:

	def connect_database():
	
		DATABASE_URL=os.environ['DATABASE_URL']

        	# Open database connection
        	conn=psycopg2.connect(DATABASE_URL,sslmode='require')

		# Prepare a cursor object
		cursor = conn.cursor()

		return cursor
        
	def intialization_of_db():

		cursor=initiateDB.connect_database()

		query1="CREATE TABLE user_table(USR_NO SERIAL PRIMARY KEY NOT NULL, NAME_OF_USER VARCHAR(30) NOT NULL, MOBILE_NUMBER NUMBER NOT NULL, EMAIL_ID VARCHAR(30) NOT NULL, CAR_NO VARCHAR(10) NOT NULL)"

		query2="CREATE TABLE admin_table(ADM_NO SERIAL PRIMARY KEY NOT NULL, ADMIN_NAME VARCHAR(30) NOT NULL, MOBILE_NUMBER NUMBER NOT NULL,ADMIN_USER_NAME VARCHAR(20) NOT NULL, ADMIN_PASSWORD VARCHAR(16) NOT NULL)"

		query3="INSERT INTO  admin_table VALUES(1,'MAIN_ADMIN',123456789,'root','ROOT1234')"

		query4="CREATE TABLE locations (LOC_NO SERIAL PRIMARY KEY NOT NULL,LOC_NAME VARCHAR(10) NOT NULL)"

		query5="CREATE TABLE violation_record(REC_NO SERIAL PRIMARY KEY NOT NULL, TIME_STAMP TIMESTAMP NOT NULL,CAR_NO VARCHAR(10) NOT NULL,LOC_NAME VARCHAR(10) NOT NULL,VIOLATION_IMAGE BLOB NOT NULL,FINE_AMOUNT VARCHAR(30) NOT NULL)"

		try:

			# Execute SQL query using execute() method.
			cursor.execute(query1)

			cursor.execute(query2)

			cursor.execute(query3)

			cursor.execute(query4)
			
			cursor.execute(query5)


			# Commit your changes in the database
			cursor.commit()
			
			cursor.close()

		except:

			# Rollback in case there is any error
			cursor.rollback()
			
			cursor.close()
			
init=initiateDB()
init.intialization_of_db()
