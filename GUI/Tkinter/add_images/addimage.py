from tkinter import *
from PIL import Image,ImageTk #pillow lib

root = Tk()
#Set size of window
root.geometry("644x434")

#set  min size (width,height)
root.minsize(500,300)

#set  maximum size (width,height)
root.maxsize(743,434)

#logic part

image = Image.open("new.jpg")
photo = ImageTk.PhotoImage(image)

'''
#without pillow
photo = PhotoImage(file="1.png")
image_label = Label(image = photo)
image_label.pack()
'''

root.mainloop()