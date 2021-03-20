from tkinter import *

root = Tk()

root.geometry("655x444")
root.title("Tips and Tricks")

#icon
root.wm_iconbitmap("file.ico") #add icon 

#background
root.configure(background = "grey")

#close button
Button(text = "Close" , command = root.destroy ).pack()



root.mainloop()