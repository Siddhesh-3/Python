from tkinter import *

root = Tk()
root.geometry("455x350")
root.title("ListBox ")

#function

def add():
    global i
    lbx.insert(ACTIVE, f"value : {i}")
    i+=1  
    
i = 0

#
lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"First Item of Listbox")

Button(root , text = "Add" , command=add).pack()


root.mainloop()