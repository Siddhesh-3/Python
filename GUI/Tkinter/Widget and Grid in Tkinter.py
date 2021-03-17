from tkinter import *

root = Tk()

root.geometry("655x333")

#Grid Layout
user = Label(root,text="Username :")
password = Label(root,text="Password :")

user.grid()
password.grid(row=1)

#function

def getvalue():
    print(uservalue.get())
    print(passvalue.get())
    print(f"Password value is {passvalue.get()}")


#classes in tkinter
  #BooleanVar,DoubleVar,IntVar,StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)  
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvalue).grid(row=3,column=1)






root.mainloop()