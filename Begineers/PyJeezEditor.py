import tkinter
from tkinter import *
from tkinter import filedialog, messagebox, scrolledtext

filename = None

def newFile():
	global filename
	filename = "Untitled"
	ans = messagebox.askquestion(title = 'Save File', message = 'Would you like to save this file?')
	if ans == True:
		saveAs()
	else:
		delete_all()

def saveAs():
	f = filedialog.asksaveasfile(mode = 'w',filetypes = (('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*')))
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		messagebox.showerror(title = 'Oops!', message = 'Unable to save file..')

def openFile():
	f = filedialog.askopenfile(mode = 'r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

def cut():
	root.clipboard_clear()
	text.clipboard_append(string = text.selection_get())
	text.delete(index1 = SEL_FIRST, index2 = SEL_LAST)

def copy():
	root.clipboard_clear()
	text.clipboard_append(string = text.selection_get())

def paste():
	text.insert(INSERT, root.clipboard_get())

def delete():
	text.delete(index1 = SEL_FIRST, index2 = SEL_LAST)

def select_all():
	text.tag_add(SEL,1.0, END)

def delete_all():
	text.delete(1.0, END)

def aboutEditor():
    label = messagebox.showinfo("About PyJeezEditor", "PyJeezEditor \n Text Editor GUI \n using Python Tkinter")

def contactMe():
	label = messagebox.showinfo("Developed By","=>> Akash Jeez <<= \n You can reach me via \n Email Address : akasht63@gmail.com \n Instagram : akash_jeez \n Blog : akashjeez.blogspot.in \n Twitter : @Gangsta_Jeez63")

root = tkinter.Tk()
root.title("PyJeezEditor")
root.minsize(width = 600, height = 600)
root.maxsize(width = 600, height = 600)

text = scrolledtext.ScrolledText(root, width = 600, height = 600, font = ("Andale Mone",12))
text.focus_set()
text.grid(row = 0, column = 0, sticky = N+S+E+W)
text.config(wrap = WORD, undo = True, width = 64)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label = 'New File', command = newFile)
filemenu.add_command(label = 'Open File', command = openFile)
filemenu.add_command(label = "Save As",command = saveAs)
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label = "Undo", command=text.edit_undo)
editmenu.add_command(label = "Redo", command=text.edit_redo)
editmenu.add_separator()
editmenu.add_command(label = 'Cut', command = cut)
editmenu.add_command(label = 'Copy', command = copy)
editmenu.add_command(label = 'Paste', command = paste)
editmenu.add_separator()
editmenu.add_command(label = 'Select All', command = select_all)
editmenu.add_command(label = 'Delete', command = delete)
editmenu.add_command(label = 'Delete All', command = delete_all)
menubar.add_cascade(label = "Edit",menu = editmenu)

helpmenu = Menu(menubar)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "About Editor", command = aboutEditor)
helpmenu.add_command(label = "Created By", command = contactMe)

root.config(menu=menubar)
root.mainloop()