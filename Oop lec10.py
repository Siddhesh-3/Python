#Class and Object
'''
class human:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def walk(self,a,b):
        self.a=a
        self.b=b
        print("Point",self.a,"to B",self.b)

obj1=human("aman","15","male")
obj1.walk(20,50)   
print(obj1.name)
print(obj1.gender)
'''
#__Init__ constructor
#self keyword
'''
class bird:
    def __init__(self,name,color,size):
        self.name=name
        self.color=color
        self.size=size
    
    def quality(self):
        print("I'm ",self.name)
        print("my color is",self.color)
        print("my size",self.size)

obj1=bird("crow","black","20")     
obj1.quality()   

'''
#without constructor
'''
class demo:
    def withoutc(self):
        print("something")
obj1=demo()
obj1.withoutc()      
'''


