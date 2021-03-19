from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("ScrollBar")

#for connecting scroll bar
Scrollbar_1 = Scrollbar(root)
Scrollbar_1.pack(side = RIGHT,fill=Y)

#widget

listbox_1 = Listbox(root, yscrollcommand = Scrollbar_1.set)

for i in range(200):
    listbox_1.insert(END, f"Item {i}")
    
listbox_1.pack(fill = "both", padx=22)
Scrollbar_1.config(command = listbox_1.yview)





root.mainloop()    
    