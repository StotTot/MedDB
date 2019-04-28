import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import sqlite3



win=tk.Tk()
win.title("Login to MedDB") #Gui title
win.geometry("250x100") #Sets GUI screen size

#button function 
def clickHere():
	username = uname.get() #To possibly be changed with SQL stuff
	password = passname.get()
        db = sqlite3.connect('/home/aristotle/Documents/project/project.odb')
        c = db.cursor()
        login = c.execute("SELECT * from LOGIN USERS uname = ? AND pass = ?", (username, password))

	if (len(login.fetchcall()) > 0):  #Checks if the user is valid, closes window, can be coded to open a new window
		messagebox.showinfo("Welcome", "Login Successful!")
		win.destroy()
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

#Buttons
logBut=ttk.Button(win, text="Login", command=clickHere) #LoginButton, when clicked calls clickHere function
logBut.grid(column=0, row=5)
win.mainloop() #main loop of GUI till its destroyed


conn.close()