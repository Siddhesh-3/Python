
from tkinter import *

root = Tk()
root.geometry("644x470")
root.title("Calculator By CodeWithHarry")
# root.wm_iconbitmap("1.ico")


#functions

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        
        
#GUI
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

#Line one
######################
f = Frame(root, bg="grey")

b = Button( text="7", padx = 23, pady=13, font="lucida 25 bold")
b.place(x=10, y = 80)
b.bind("<Button-1>", click)

b = Button(text="8", padx=23, pady=13, font="lucida 25 bold")
b.place(x=110, y = 80)
b.bind("<Button-1>", click)

b = Button( text="9", padx=23, pady=13, font="lucida 25 bold")
b.place(x=210, y = 80)
b.bind("<Button-1>", click)

b = Button( text="0", padx=23, pady=13, font="lucida 25 bold")
b.place(x=310, y = 80)
b.bind("<Button-1>", click)

b = Button( text="-", padx=23, pady=13, font="lucida 25 bold")
b.place(x=410, y = 80)
b.bind("<Button-1>", click)

b = Button( text="*", padx=23, pady=13,font="lucida 25 bold")
b.place(x=510, y = 80)
b.bind("<Button-1>", click)

f.pack()

###################################
#LINE 2

f = Frame(root, bg="grey")

b = Button(text="4", padx=23, pady=13, font="lucida 25 bold")
b.place(x=10, y = 180)
b.bind("<Button-1>", click)

b = Button( text="5", padx=23, pady=13, font="lucida 25 bold")
b.place(x=110, y = 180)
b.bind("<Button-1>", click)

b = Button( text="6", padx=23, pady=13, font="lucida 25 bold")
b.place(x=210, y = 180)
b.bind("<Button-1>", click)

b = Button(text="/", padx=27, pady=13, font="lucida 25 bold")
b.place(x=310, y = 180)
b.bind("<Button-1>", click)

b = Button(text="%", padx=15, pady=13, font="lucida 25 bold")
b.place(x=410, y = 180)
b.bind("<Button-1>", click)

b = Button(text="=", padx=20, pady=13, font="lucida 25 bold")
b.place(x=510, y = 180)
b.bind("<Button-1>", click)


f.pack()


f = Frame(root, bg="grey")

b = Button( text="1", padx=23, pady=13, font="lucida 25 bold")
b.place(x=10, y = 280)
b.bind("<Button-1>", click)

b = Button(text="2", padx=23, pady=13, font="lucida 25 bold")
b.place(x=110, y = 280)
b.bind("<Button-1>", click)

b = Button( text="3", padx=23, pady=13, font="lucida 25 bold")
b.place(x=210, y = 280)
b.bind("<Button-1>", click)

b = Button(text="C", padx=20, pady=13, font="lucida 25 bold")
b.place(x=310, y = 280)
b.bind("<Button-1>", click)

b = Button(text=".", padx=23, pady=13, font="lucida 25 bold")
b.place(x=410, y = 280)
b.bind("<Button-1>", click)

b = Button(text="00", padx=12, pady=13, font="lucida 25 bold")
b.place(x=510, y = 280)
b.bind("<Button-1>", click)


f.pack()





root.mainloop()
