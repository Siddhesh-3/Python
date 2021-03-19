from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("455x233")
root.title("Slider in Tkinter")

#function

def getdollar():
    tmsg.showinfo("Ammount Creadited !",f"Dollar {my_Slider2.get()} is crated to your accout")


#slider
Label(root, text="How many Dollars do you want ?").pack()

# my_Slider = Scale(root, from_= 0, to = 100) #vertical slider
# my_Slider.pack()

my_Slider2 = Scale(root, from_= 0, to = 100, orient = HORIZONTAL, tickinterval =50) #horizontal slider
my_Slider2.set(20)
my_Slider2.pack()

Button(root, text="Get dollars" ,pady = 10, command=getdollar).pack()




root.mainloop()