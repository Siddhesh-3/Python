from tkinter import *


class GUI(Tk):
    def __init__(self): #self is root here
        super().__init__()
        
        self.geometry("744x377")
    
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar =s self.var, relief = SUNKEN, anchor = "w")
        self.statusbar.pack(side = BOTTOM, fill = X )
    
    def click(self):
        print("Button Clicked")
        
    def createbutton(self, inptext):
        Button(text = inptext, command = self.click).pack()  
        
if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton("Click Me!")
    window.mainloop()
            
        



