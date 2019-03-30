from tkinter import *
from tkinter import messagebox
import smtplib

window = Tk()
window.title("Send Mail from Gmail")
window.geometry('400x300')

sender_email_text = StringVar()
sender_email_password_text = StringVar()
receiver_email_text = StringVar()
message_text = StringVar()

def sendEmail():
	server = smtplib.SMTP_SSL('smtp.gmail.com')
	server.login(sender_email_text.get(), sender_email_password_text.get())
	message = f"Subject: Python Tkinter GUI \n\n {message_text.get()}"
	server.sendmail(sender_email_text.get(), receiver_email_text.get(), message)
	server.quit()
	messagebox.showinfo('Success!', f"Mail Sent to {receiver_email_text.get()} successfully!")

def aboutMe():
	developer_info = """
	Name 	: AkashJeez
	Email 	: akashit63@gmail.com
	Instagram	: akash_jeez
	Blog 	: akashjeez.blogspot.com
	Twitter	: Akash Jeez (@Gangsta_Jeez63)
	"""
	messagebox.showinfo('About Developer', developer_info)

top_label = Label(window, text = "Compose New Mail from Gmail \n Using Python Tkinter GUI", fg = 'blue', bg = 'red', font=("Arial Bold", 13)).grid(row=0, columnspan=4)
sender_email_label = Label(window, text = "Sender Email ID", fg = 'blue', font=("Arial Bold", 9)).grid(row = 2, column = 0, padx = 5, pady = 5, sticky='sw')
sender_email_password_label = Label(window, text = "Sender Email ID Password", fg = 'blue', font=("Arial Bold", 9)).grid(row = 3, column = 0, padx = 5, pady = 5, sticky='sw')
receiver_email_label = Label(window, text = "Receiver Email ID", fg = 'blue', font=("Arial Bold", 9)).grid(row = 4, column = 0, padx = 5, pady = 5, sticky='sw')
message_label = Label(window, text = "Message Body", fg = 'blue', font=("Arial Bold", 9)).grid(row = 5, column = 0, padx = 5, pady = 5, sticky='sw')

sender_email_entry = Entry(window, textvariable = sender_email_text, width = 30).grid(row = 2, column = 1, padx = 5, pady = 5, sticky='sw')
sender_email_password_entry = Entry(window, textvariable = sender_email_password_text, show = '*', width = 30).grid(row = 3, column = 1, padx = 5, pady = 5, sticky='sw')
receiver_email_entry = Entry(window, textvariable = receiver_email_text, width = 30).grid(row = 4, column = 1, padx = 5, pady = 5, sticky='sw')
message_entry = Entry(window, textvariable = message_text, width = 35).grid(row = 5, column = 1, padx = 5, pady = 5, sticky='sw')

send_mail_button = Button(window, text = "Send Mail", width = 12, bg = 'green', fg = 'white', font=("Arial Bold", 8, 'bold'), command = sendEmail).grid(row = 7, column = 0, padx = 5, pady = 5)
close_button = Button(window, text = "Close", width = 12, bg = 'red', fg = 'white', font=("Arial Bold", 8, 'bold'), command = window.destroy).grid(row = 7, column = 1, padx = 5, pady = 5)
aboutme_button = Button(window, text = "About Developer", width = 12, bg = 'blue', fg = 'white', font=("Arial Bold", 8, 'bold'), command = aboutMe).grid(row = 9, columnspan = 2, padx = 5, pady = 5)

window.mainloop()