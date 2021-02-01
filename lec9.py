#GUI              #you can use pyqt or kivy
dic_credentials = {
    'admin' : 'India123',
    'Arvind' : '123456',
    'Ravi' : 'ravi1234@',
    'Atharva' : 'Atharva1234@',
}

def dosomething():
  username = user_entry.get()
  password = pwd_entry.get()

  if dic_credentials[username] == password :
      print("Login Succsess")
  else:
      print("Invalid Credentials")

import tkinter as tk 

gui = tk.Tk()
gui.geometry('350x200')

#username lable
user_lable = tk.Label(master = gui ,text = "Username" )
#username entry
user_entry = tk.Entry(master = gui)
#Password Lable
pwd_lable = tk.Label(master = gui,text = "Password")
#Password Entry
pwd_entry = tk.Entry(master= gui,show ="*")
#button
btn_login = tk.Button(master= gui ,text= 'Login',command = dosomething) #link to function
#pack
user_lable.pack()
user_entry.pack()
pwd_lable.pack()
pwd_entry.pack() 
btn_login.pack()

gui.mainloop()
