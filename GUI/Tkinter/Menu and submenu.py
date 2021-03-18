from tkinter import *

root = Tk()
root.title("Pycharm")
root.geometry("655x555")


#function_name
def function_name():
    pass



# use this to create non-dropdown menu
'''
mymenu = Menu(root)
mymenu.add_command(label="File", command=function_name)
mymenu.add_command(label="Exit", command=quit)
root.config(menu=mymenu)
'''
#dropdown

#file menu

file_menu = Menu(root)

m1 = Menu(file_menu, tearoff = 0) #tearoff avoid dotted line 

m1.add_command(label = "New project", command = function_name)
m1.add_separator() #add seperator line
m1.add_command(label = "Save", command = function_name)
m1.add_command(label = "Save as", command = function_name)
m1.add_command(label = "Print", command = function_name)
root.config(menu=file_menu)

file_menu.add_cascade(label = "File",menu = m1 )

m2 = Menu(file_menu, tearoff = 0) #tearoff avoid dotted line 

#edit menu

m2.add_command(label = "New project", command=function_name)
m2.add_separator() #add seperator line
m2.add_command(label = "Save", command = function_name)
m2.add_command(label = "Save as", command = function_name)
m2.add_command(label = "Print", command = function_name)
root.config(menu=file_menu)

file_menu.add_cascade(label = "Edit",menu = m2 )







root.mainloop()