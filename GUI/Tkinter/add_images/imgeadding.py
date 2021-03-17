from tkinter import *
from PIL import Image,ImageTk #pillow lib

root = Tk()


image = Image.open("new.jpg")
photo = ImageTk.PhotoImage(image)


root.mainloop()
