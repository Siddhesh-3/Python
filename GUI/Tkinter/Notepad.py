
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

#function

def newFile:
    pass

def 









if __name__ == '__main__':
    #basic setup
    
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")
    
    #Text area
    TextArea = Text(root, font = "lucida 13")
    file = None

    #Lets create menubar
    
    MenuBar = Menu(root)
    #File menu start
    FileMenu = Menu(MenuBar, tearoff = 0)
    
    #to open file
    FileMenu.add_command(label = "New", command = newFile)
    
    #TO Open already existing file 
    FileMenu.add_command(label = "Open", command = openFile)
    
    # To save the current file
    
    FileMenu.add_command(label = "Save", command=saveFile)
    FileMenu.add_separator() 
    
    #exit
    FileMenu.add_command(label = "Exit", command = quitApp)
    
    MenuBar.add_cascade(label = "File", menu = FileMenu)
    #file menu ends
    
    #edit menu start
    EditMenu = Menu(MenuBar, tearoff = 0)
    
    #to give a feature of cut ,copy and paste
    EditMenu.add_command(label = "Cut", command = cut)
    EditMenu.add_command(label = "Copy", command = copy)
    EditMenu.add_command(label = "Paste", command = paste)
    
    EditMenu.add_cascade(label = "Edit", menu = EditMenu)
    #Edit menu end
    
    #help menu start
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label = "About Notepad", command = about)
    MenuBar.add_cascade(label = "Help", menu = help)
    #help menu ends
    root.congig(menu = MenuBar)
    
    root.mainloop()