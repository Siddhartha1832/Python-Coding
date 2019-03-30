'''
Install below Python Module before You run this code.
>>> pip install pywin32
'''

import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

def send_email(to, subject, body):
	mail.To = to
	mail.Subject = subject
	mail.HTMLBody = '<h2> {} </h2>'.format(body)
	#mail.Attachments.Add(attachment)
	print('\n Mail sent to {} sucessfully!!'.format(to))

if __name__ == '__main__':
	print('\n Composing New Email from Outlook.. \n')
	to = input(' Enter Recepient Email Address: ')
	subject = input(' Enter Mail Subject: ')
	body = input(' Enter Mail Content: ')
	#attachment = input(' Enter local file URL to attach into mail: ')
	send_email(to, subject, body)