'''
class - blueprint
object - everything

pillars of oop
inheritance

'''
# 1.Inheritance 
# 2.Abstraction (hiding unnecessary details from the user)
# 3.Encapsulation(to store thing together,privately,protected,protect from misuse)
# 4.Polymorphism(having multiple forms)(function having same name)
    #overriding
    #overloading
'''
class parent:
    def color(self):
        print("color is blue")

class child(parent):
    pass

#parent class
obj1=parent()
obj1.color()
#see when we pass parent class to child we can access parent data in child
obj2=child()
obj2.color()
'''
#Abstraction (hiding unnecessary details from the user)

#Encapsulation(to store thing together,privately,protected,protect from misuse)
'''
class atm:
    def __init__(self,name,balance,pin):
        self.name = name
        self.balance = balance
        self.__pin = pin  #magic method for varible private method

sid = atm("sid",10000,1234)
print(sid.name)
print(sid.balance)
#print(sid.pin) #you can not access pin
print(sid._atm__pin)
'''
#Polymorphism(having multiple forms)

class atm:
    def withdraw():
        print("Money withdraw")
class deposit_atm(atm):
    def withdraw():
        print("You cannot withdraw here")    
obj1=atm()

atm.withdraw()

deposit_atm.withdraw()