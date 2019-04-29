import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import sqlite3




def mainWindow(): #main window for after login
	mainWin=tk.Tk()
	mainWin.title("MedDB")
	conn = sqlite3.connect('Med_DB.db')
	messagebox.showinfo("This is a test!", "Connected to database!")
	#tempList=[['101','Brian','M','02/21/2010'],['102','Kailey','F','05/12/2011'],['103','Dave','M','03/18/2011']]
	label=tk.Label(mainWin, text="SomeData:")
	label.grid(row=0, columnspan=3)

	#Values of columns
	cols=('Patient Number', 'Name', 'Gender', 'Last Admited')
	listbox=ttk.Treeview(mainWin, columns=cols, show='headings')

	for col in cols:
		listbox.heading(col, text=col)
	listbox.grid(row=1, column=0, columnspan=2)

	cursor = conn.execute("SELECT PAT_NUM, NAME, GENDER, LAST_ADMIT from PATIENTS")
	
	for row in cursor:
		listbox.insert("", "end", values =(row[0], row[1], row[2], row[3]))

	mainWin.mainloop()

win=tk.Tk()
win.title("Login to MedDB") #Gui title
win.geometry("250x100") #Sets GUI screen size

#button function 
def clickHere():
	username=uname.get() #To possibly be changed with SQL stuff
	password=passname.get()
	if username=="user" and password=="test":  #Checks if the user is valid, closes window, can be coded to open a new window
		messagebox.showinfo("Welcome", "Login Successful!")
		win.destroy()
		mainWindow() #calls to main window function
	else:
		messagebox.showwarning("Error", "Invalid Credentials")

#Labels
aLabel=ttk.Label(win, text="Username:") #Displays the text Username and Password
bLabel=ttk.Label(win, text="Password:")
aLabel.grid(column=0, row=1) #sets the User and pass labels ontop of eachother
bLabel.grid(column=0, row=3)

#Text box
uname=tk.StringVar()  #becomes the text box variable
unameEnter=ttk.Entry(win, width=12, textvariable= uname) #username text box
unameEnter.grid(column=2, row=1) #Username text box spacing
passname=tk.StringVar()
passnameEnter=ttk.Entry(win, width=12, show ='*', textvariable=passname) #Show '*' so that password is hidden
passnameEnter.grid(column=2, row=3) #for project hash password

unameEnter.focus()
#Buttons
logBut=ttk.Button(win, text="Login", command=clickHere) #LoginButton, when clicked calls clickHere function
logBut.grid(column=0, row=5)
win.mainloop() #main loop of GUI till its destroyed