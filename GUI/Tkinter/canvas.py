from tkinter import *

root = Tk()

canvas_width = 800
canvas_height= 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)              
can_widget.pack()


# The line goes from the point x1,y1 to x2,y2

can_widget.create_line(0,0,800,200)

can_widget.create_line(55,25,800,200,fill="red")

#rectangle toprightpoint(x1,y1),bottomleft(x2,y2)
can_widget.create_rectangle(355,255,150,130,fill='green')

#fit text inside gui

can_widget.create_text(400,200,text="Python Text")

#oval making using rectangle co-ordinate

can_widget.create_oval(444,144,522,300)









root.mainloop()