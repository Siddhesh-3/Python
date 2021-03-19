from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("455x266")
root.title("Radio Button")

#function

def order_food():
    tmsg.showinfo("Confirmed",f"Your {var.get()} Order is Placed !")

#
# var = IntVar()

var = StringVar()
var.set("Radio")

Label(root, text = "What would you like to have sir ?",font = "lucida 10 bold", justify = LEFT, padx = 14).pack()

radio = Radiobutton(root, text="Dosa", padx=14, variable = var, value = "Dosa").pack(anchor = "w")
radio = Radiobutton(root, text="Vadapav", padx=14, variable = var, value = "Vadapav").pack(anchor = "w")
radio = Radiobutton(root, text="Misal", padx=14, variable = var, value = "Misal").pack(anchor = "w")
radio = Radiobutton(root, text="Tea",  variable = var, value = "Tea").pack(anchor = "w")

Button(root, text="Confirm Order!", command = order_food, padx = 12, pady = 12).pack(anchor="w",padx = 12, pady = 12)

root.mainloop()