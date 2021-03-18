from tkinter import *

root = Tk()
root.title("Events in Tkinter")
root.geometry("644x344")

#function event

def func_1(event):
    print(f"You Clicked on the button at {event.x} ,{event.y}")
    
widget = Button(root, text="Click me")
widget.pack()

#event
widget.bind('<Button-1>',func_1)
widget.bind('<Double-1>',quit)
root.mainloop()