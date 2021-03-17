from tkinter import *

root = Tk()

root.title("My GUI")

'''
Lable Options
text -add text
bd - background
fg -foreground
font- set font
padx - x padding 
pady - y padding
relief - border styling - SUNKEN ,RAISED ,GROOVE ,RIDGE

'''
title_lable = Label(text = '''
                    rogramming is like art—both the process of writing code and the code in itself.
                    \nConverting an idea that only existed in your head into reality is an unparalleled feeling. 
                    \nIt’s a kind of mindfulness that keeps you in a state of flow when you love the work you do.
                    \nAnd, when your product impacts millions of developers and helps them find the right place to work—it’s both exciting and scary! ''', 
                    bg="red",fg="white",padx=23,pady=50,font=("comicsansms",10,"bold"),borderwidth=3,relief=SUNKEN) #font=(fontname size bold)

#Important Pack Options
#anchor=nw
#side =top ,bottom,left,right

#title_lable.pack(anchor="sw")

#title_lable.pack(side=BOTTOM)
#title_lable.pack(fill=X) #increse at x axis 
title_lable.pack(side=LEFT,fill=Y,padx=34,pady=25)





root.mainloop()