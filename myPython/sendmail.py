import smtplib
from email.mime.text import MIMETextclass

	def send_mail(self,time_stam,car_no,loc_name,fine_amount,email_id,name_of_user):
	
		API_KEY = os.environ.get('MAILGUN_API_KEY')
		API_MAIL_DOMAIN = os.environ.get('MAILGUN_DOMAIN')
		API_URL = "https://api:#{API_KEY}@api.mailgun.net/v2/{API_MAIL_DOMAIN}"
		API_USERNAME = os.environ.get('MAILGUN_SMTP_LOGIN')
		API_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
		MAILGUN_SMTP_SERVER = os.environ.get('MAILGUN_SMTP_SERVER')

		msg = MIMEText('Testing some Mailgun awesomness')
		msg['Subject'] = "Hello"
		msg['From']    = "root@"+API_MAIL_DOMAIN
		msg['To']      = email_id
		
		s = smtplib.SMTP(MAILGUN_SMTP_SERVER, 587)
		
		s.login(API_USERNAME, API_PASSWORD)
		s.sendmail(msg['From'], msg['To'], msg.as_string())
		s.quit()


		
		'''sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
		from_email = Email(request.form.get("vivianfernandes6795@gmail"))
		to_email = Email(request.form.get("to_email"))
		subject = "Test Mail to Display Voilation!"
		str_content="User,\n \n Seems like you have voilated traffic rules! Below are the details:\v Time Stamp \t : \t"+str(time_stam)+"\nCar Number \t : \t"+car_no+"\nLocation \t : \t"+loc_name+"\nFine Amount \t : \t"+str(fine_amount)
		content = Content("text/plain", str_content)
		mail = Mail(from_email, subject, to_email, content)
		response = sg.client.mail.send.post(request_body=mail.get())
		#response = sg.client.mail.send.post(request_body=mail.get())
		print(response.status_code)
		print(response.body)
		print(response.headers)
		verbose="Sent Mail to User "+name_of_user
		return verbose'''