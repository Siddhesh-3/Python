print("1. Add Name")
print("2. Delete Name")
print("3. Update Name")
print("4. Exit")
choice = int(input("Enter Your Choice"))
if choice == 1:
    a = int(input("Enter No 1"))
    b = int(input("Enter No 2"))
    result = a+b
    print("Addition is",result)
    if result < 5:
        print("Number is less than 5")
    else:
        print("number is greater than five")
if choice == 2:
    print("Loop 2")   
elif choice == 3:
    print("Loop3")
