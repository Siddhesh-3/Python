from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Pycharm")
root.geometry("655x555")


#function_name
def function_name():
    pass

def help_us():
    tmsg.showinfo("Help","Siddhesh will solve your problem")
    
def rate_us():
    rate_value = tmsg.askquestion("Rate us", "Was your experience good ?")
    if rate_value == "yes":
        msg = "Thank You.Please rate us on app store"
    else:
        msg = "Tell us what went wrong. We will reach you soon"
    tmsg.showinfo("Experience",msg)   
    
def retry_use():
    ans = tmsg.askretrycancel("Question","wanna friend with siddhesh ?")
    
    if ans:
        tmsg.showinfo("Ans","Siddhesh Don't want friendship with you !")
    else:
        tmsg.showinfo("Ans","okay")    
         
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


#edit menu
m2 = Menu(file_menu, tearoff = 0) #tearoff avoid dotted line 

m2.add_command(label = "New project", command=function_name)
m2.add_separator() #add seperator line
m2.add_command(label = "Save", command = function_name)
m2.add_command(label = "Save as", command = function_name)
m2.add_command(label = "Print", command = function_name)
root.config(menu=file_menu)

file_menu.add_cascade(label = "Edit",menu = m2 )

#
m3 = Menu(file_menu, tearoff = 0) #tearoff avoid dotted line 

m3.add_command(label = " Help ", command=help_us)
m3.add_separator() #add seperator line
m3.add_command(label = "Rate us", command = rate_us)
m3.add_command(label = "retry", command = retry_use)

root.config(menu=file_menu)

file_menu.add_cascade(label = "Edit",menu = m3 )






root.mainloop()