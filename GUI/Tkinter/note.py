from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("Note Using scrollbar")

#for connecting scroll bar
Scrollbar_1 = Scrollbar(root)
Scrollbar_1.pack(side = RIGHT,fill=Y)

#widget


text = Text(root,yscrollcommand = Scrollbar_1.set)
text.pack(fill = BOTH)
Scrollbar_1.config(command = text.yview)




root.mainloop()    
    