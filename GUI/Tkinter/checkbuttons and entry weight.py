from tkinter import *

root = Tk()

root.geometry("633x333")

#function
def getvals():
    print("Submiting new from")
    print(f"{name_value.get(), phone_value.get(), gender_value.get(), emergency_value.get(), paymentmode_value.get(), foodservices_value.get()}")
    
    with open("record.txt" ,"a") as f:
        f.write(f"{name_value.get(), phone_value.get(), gender_value.get(), emergency_value.get(), paymentmode_value.get(), foodservices_value.get()}\n")


#display text for from
Label(root, text="Welcome to Sid Travels",pady=15, font="comicsansms 13 bold").grid(row=0,column=5)
name = Label(root, text ="Name :")
phone = Label(root, text="Phone :")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Payment Mode")

#pack as grid
name.grid(row=1,column=1) 
phone.grid(row=2,column=1)
gender.grid(row=3,column=1)
emergency.grid(row=4,column=1)
paymentmode.grid(row=5,column=1)

#values for storing entry

name_value = StringVar()
phone_value = IntVar()
gender_value = StringVar()
emergency_value = IntVar()
paymentmode_value = StringVar()
foodservices_value = IntVar() #checkbox varible

#Entry box for from
name_entry = Entry(root, textvariable= name_value)
phone_entry = Entry(root, textvariable= phone_value)
gender_entry = Entry(root, textvariable= gender_value)
emr_entry = Entry(root, textvariable= emergency_value)
paymode_entry = Entry(root, textvariable= paymentmode_value)

#pack entry
name_entry.grid(row=1,column=3)
phone_entry.grid(row=2,column=3)
gender_entry.grid(row=3,column=3)
emr_entry.grid(row=4,column=3)
paymode_entry.grid(row=5,column=3)

#checkbox

foodservice = Checkbutton(text="Want to prebook your meals ?", variable = foodservices_value)
foodservice.grid(row=6,column=3)

#Button 

Button(text="Submit to Sid Travels" ,command=getvals).grid(row=7,column=3)






root.mainloop()