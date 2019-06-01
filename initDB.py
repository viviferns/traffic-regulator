import os
import urllib.parse as urlparse
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
db=SQLAlchemy(app)

class Person(db.Model):

	ADM_NO=db.Column(db.Integer,primary_key=True)
	ADMIN_NAME=db.Column(db.String(20),unique=False)
	MOBILE_NUMBER=db.Column(db.Integer,unique=True)
	ADMIN_USER_NAME=db.Column(db.String(10),unique=True)
	ADMIN_PASSWORD=db.Column(db.String(16),unique=False)
	
	def __init__(self,ADM_NO,ADMIN_NAME,MOBILE_NUMBER,ADMIN_USER_NAME,ADMIN_PASSWORD):
		self.ADM_NO=ADM_NO
		self.ADMIN_NAME=ADMIN_NAME
		self.MOBILE_NUMBER=MOBILE_NUMBER
		self.ADMIN_USER_NAME=ADMIN_USER_NAME
		self.ADMIN_PASSWORD=ADMIN_PASSWORD
		
		
if __name__ == '__main__':
	#app.run(debug = True)
	db.create_all()
	