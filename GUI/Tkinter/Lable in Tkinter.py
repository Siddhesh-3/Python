from tkinter import *

root = Tk()

#Set size of window
root.geometry("644x434")

#set  min size (width,height)
root.minsize(500,300)

#set  maximum size (width,height)
root.maxsize(743,434)


#gui logic
pycharm_photo = Label(text="Image")
pycharm_photo.pack()

name = Label(text="PyCharm Community Edition")
name.pack()

version = Label(text="Version 2017.2")
version.pack()

create_project = Label(text="Create new Project")
create_project.pack()

open_project = Label(text= "Open")
open_project.pack()





root.mainloop()