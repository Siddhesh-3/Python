from tkinter import *

root = Tk()
root.geometry("300x250") #set default size

#function
def windowsize():
    # if width_of_window != width_value and height_of_window != height_value:  
    #      error = Label(root,text="Enter valid values",fg="red")
    #      error.grid(row=7,column=1)
    # else:
        root.geometry(f"{width_value.get()}x{height_value.get()}")

#text

width_name = Label(root, text="Enter Width :")
width_name.grid(row=0,column=0)  

height_name = Label(root, text="Enter Height :")
height_name.grid(row=1,column=0)  

#value
width_value = IntVar()
height_value = IntVar()

width_of_window = Entry(root ,textvariable = width_value )
width_of_window.grid(row=0,column=1,pady=20)

height_of_window = Entry(root ,textvariable = height_value)
height_of_window.grid(row=1,column=1,pady=20)
    

Button(root,text = "Submit Size",command=windowsize,font=("comicsansms 13 bold")).grid(row=6,column=1,pady=20)       
    


#windowsize(width_of_window, height_of_window)




root.mainloop()