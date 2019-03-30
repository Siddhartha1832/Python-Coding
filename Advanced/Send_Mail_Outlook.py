import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

def send_email(to, subject, body, attachment):
	mail.To = to
	mail.Subject = subject
	mail.Body = body
	mail.HTMLBody = '<h2> {} </h2>'.format(body) #this field is optional
	mail.Attachments.Add(attachment)
	mail.Send()
	print('\n Mail sent to {} sucessfully!!'.format(to))

if __name__ == '__main__':
	print('\n Composing New Email.. \n')
	to = input(' Enter Recepient Email Address: ')
	subject = input(' Enter Mail Subject: ')
	body = input(' Enter Mail Content: ')
	attachment = input(' Enter local file URL to attach into mail: ')
	send_email(to, subject, body, attachment)
