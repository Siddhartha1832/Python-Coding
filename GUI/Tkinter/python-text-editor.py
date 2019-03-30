from tkinter import Tk, scrolledtext, filedialog, messagebox, Menu, END
from tkinter import *

root = Tk()
root.title("PyJeezEditor")
root.geometry("600x600")
textPad = scrolledtext.ScrolledText(root, width=600,height=600,font=("Andale Mone",12))
textPad.focus_set()

def new_file():
	textPad.delete(0.0, END)

def open_file():
	file = filedialog.askopenfilename(parent=root, title='Select a file', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")]) 
	try:
		file = open(file, 'r')
		textPad.insert(0.0, file.read())
		file.close()
	except:
		messagebox.showerror("Oops!", "Unable to open the file.")

def save_file():
	file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
	data = textPad.get(0.0, END)
	try:
		file.write(data)
		file.close()
	except:
		messagebox.showerror("Oops!", "Unable to save the file.")
        
def exit_command():
	if messagebox.askokcancel("Quit", "Do you really want to quit?"):
		root.destroy()

def cut_command():	textPad.event_generate('<<Cut>>')

def copy_command():	textPad.event_generate('<<Copy>>')

def paste_command():	textPad.event_generate('<<Paste>>')

def about_editor():
	label = messagebox.showinfo("About PyJeezEditor", f" PyJeezEditor \n Tkinter GUI based Text Editor which is written in Python")

def about_developer():
	info = '''
	> Name : Akash (Nickname: AkashJeez) \n
	> Email : akashit63@gmail.com \n
	> Website : https://akashjeezpython.pythonanywhere.com \n
	> BlogSpot : https://akashjeez.blogspot.com \n
	> Instagram : https://www.instagram.com/akash_jeez \n
	> Twitter : https://twitter.com/gangsta_jeez63 \n
	> GitHub : https://github.com/akashjeez \n
	> Tumblr : https://akashjeez.tumblr.com \n
	> Google+ : https://plus.google.com/+AkashPonnurangam
	'''
	label = messagebox.showinfo("About Developer", f"{info}")

def dummy():	pass

# create a menu & define functions for each menu item
menubar = Menu(root)
filemenu = Menu(menubar)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "New", command = new_file, accelerator="Ctrl+N")
filemenu.add_command(label = "Open", command = open_file, accelerator="Ctrl+O")
filemenu.add_command(label = "Save", command = save_file, accelerator="Ctrl+S")
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = exit_command, accelerator="Ctrl+Q")
editmenu = Menu(menubar)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Cut", command = cut_command, accelerator="Ctrl+X")
editmenu.add_command(label = "Copy", command = copy_command, accelerator="Ctrl+C")
editmenu.add_command(label = "Paste", command = paste_command, accelerator="Ctrl+V")
helpmenu = Menu(menubar)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "About Editor", command = about_editor)
helpmenu.add_command(label = "About Developer", command = about_developer)

root.bind('<Control-n>', lambda event: new_file())
root.bind('<Control-o>', lambda event: open_file())
root.bind('<Control-s>', lambda event: save_file())
root.bind('<Control-q>', lambda event: exit_command())

textPad.pack()
root.config(menu = menubar)
root.mainloop()