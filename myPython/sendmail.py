import sendgrid
import os

class SendMail:

	def send_mail(self,time_stam,car_no,loc_name,fine_amount,email_id,name_of_user):
	
		API_KEY = os.environ.get('API_KEY')
		DOMAIN_NAME = os.environ.get('DOMAIN_NAME')

		if not (API_KEY and DOMAIN_NAME):
			return 'Invalid environment variables'

		result = requests.post(
			('https://api.mailgun.net/v3/%s/messages' % DOMAIN_NAME),
			auth = ('api', API_KEY),
			data = {
					'from': ('Traffic Department <root@%s>' % DOMAIN_NAME),
					'to': email_id,
					'subject': 'Stuff is on sale',
					'html': name_of_user+',\n \n Seems like you have voilated traffic rules! Below are the details:\v Time Stamp \t : \t'+str(time_stam)+'\nCar Number \t : \t'+car_no+'\nLocation \t : \t'+loc_name+'\nFine Amount \t : \t'+str(fine_amount)
			}
		)
		verbose="Sent Mail to User "+name_of_user
		return verbose'''

		
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