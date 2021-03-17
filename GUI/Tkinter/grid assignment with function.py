from tkinter import *

root = Tk()

root.geometry("633x333")
#function
def get_values():
    print(namevalue.get())
    print(agevalue.get())
    print(addressvalue.get())
    print(weightvalue.get())
    print(feesvalue.get())

    v = Label(text="Value Submited")
    v.grid()


#Grid display

name = Label(root,text="Name :")
age = Label(root,text="Age :")
weight = Label(root,text="Weight :")
address = Label(root,text="Address :")
feespaid = Label(root,text="Fees Paid :")

name.grid(pady=10)
age.grid(row=1,pady=10)
weight.grid(row=2,pady=10)
address.grid(row=3,pady=10)
feespaid.grid(row=4,pady=10)

#input
#BooleanVar,DoubleVar,IntVar,StringVar

namevalue = StringVar()
agevalue = IntVar()
weightvalue = DoubleVar()
addressvalue = StringVar()
feesvalue = IntVar()

name_entry = Entry(root,textvariable=namevalue)
age_entry = Entry(root,textvariable=agevalue)
weight_entry = Entry(root,textvariable=weightvalue)
address_entry = Entry(root,textvariable=addressvalue)
fees_entry = Entry(root,textvariable=feesvalue)


name_entry.grid(row=0,column=1)
age_entry.grid(row=1,column=1)
weight_entry.grid(row=2,column=1)
address_entry.grid(row=3,column=1)
fees_entry.grid(row=4,column=1)

Button(root,text="Submit",command=get_values).grid(pady=10,column=1)






root.mainloop()