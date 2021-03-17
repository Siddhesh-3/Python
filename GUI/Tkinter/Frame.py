from tkinter import *

root =Tk()
#window size
root.geometry("655x333")

#frame
f1 = Frame(root , bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT, fill="y",pady=10)

f2 =Frame(root, bg="grey",borderwidth=8 )
f2.pack(side=TOP,fill="x")

#lable inside frame
l = Label(f1 ,text="Project Tkinter -Pycharm ",fg="red")
l.pack(pady = 130)

l2 = Label(f2 ,text="Welcome to pycharm")
l2.pack()

root.mainloop()