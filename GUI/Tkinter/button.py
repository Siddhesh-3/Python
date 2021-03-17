from tkinter import *

root = Tk()

#window
root.geometry("655x333")

#logic

def hello():
    print("Hello Button")
    
def name():
    print("My name is Siddhesh")

#display

frame = Frame(root,borderwidth=6,bg="black",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

#button

b1 = Button(frame , fg="red" ,text="Print now",command=hello) #call function using command
b1.pack(side=LEFT,padx=5)

b2 = Button(frame , fg="red" ,text="Tell me name now",command=name)
b2.pack(side=LEFT,padx=5)

b3 = Button(frame , fg="red" ,text="Print now")
b3.pack(side=LEFT,padx=5)




root.mainloop()