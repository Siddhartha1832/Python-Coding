import smtplib, getpass

def sendMail(sender_email_address, sender_password, receiver_email_address, subject, body):
	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(sender_email_address, sender_password)
		message = f"Subject: {subject} \n\n {body}"
		server.sendmail(sender_email_address, receiver_email_address, message)
		print('\n Mail Sent to {} Sucessfully!!!'.format(receiver_email_address))
	except:
		print('\n Failed to Send EMail, Please try again..')

if __name__ == '__main__':
	print('\n *** Compose New Email from GMail using SMTPLib in Python *** \n')
	sender_email_address = input(' Enter Sender Email Address : ')
	sender_password = getpass.getpass(' Enter Sender Email Password : ')
	receiver_email_address = input(' Enter Receiver Email Address : ')
	subject = input(' Enter Mail Subject : ')
	body = input(' Enter Mail Content : ')
	sendMail(sender_email_address, sender_password, receiver_email_address, subject, body)
