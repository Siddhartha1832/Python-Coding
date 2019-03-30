from tkinter import *
import tkinter.messagebox as msgbox
root = Tk() 
root.title('TkinterGUI')

name = StringVar()
email = StringVar()
comments = StringVar()

def submit():
	msgbox.showinfo('Info', "Name : {} \nEmail : {}".format(name.get(), email.get()))

label1 = Label(root, text='Name').grid(row=0, column=0, padx=5, sticky='sw')
label2 = Label(root, text='Email').grid(row=0, column=1, padx=5, sticky='sw')
entry1 = Entry(root, textvariable=name).grid(row=1, column=0, padx=5, sticky='sw')
entry2 = Entry(root, textvariable=email).grid(row=1, column=1, padx=5, sticky='sw')
label3 = Label(root, text='Comments').grid(row=2, column=0, padx=5, sticky='sw')
text1 = Text(root, width=50, height=10).grid(row=3, column=0, columnspan=2, padx=3, sticky='sw')
button1 = Button(root, text='Submit', command=submit)
button1.grid(row=4, column=0, padx=5, sticky='sw')
button2 = Button(root, text='Clear').grid(row=4, column=1, padx=5, sticky='sw')

root.mainloop()