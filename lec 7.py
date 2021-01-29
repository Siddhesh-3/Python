#Genric programing

#DRY - Dont Repeat Yourself
# - Reusability
# maintablity

#Function - reusable
'''
def function_name():
    name = input("Enter Name :")
    print(name) #this is not excute untill you call them
    
function_name()   #this is function call

'''
#
'''
def Button():
    button =input('Enter button no :')
    print(button)
    
Button()

def Button2(a,b):
    print("Sum :",a+b)
    
Button2(50,50)
Button2(10,20)
'''
#return
'''
def Button():
    button =input('Enter button no :')
    print(button)
    
Button()

def Button2(a,b):
    #print("Sum :",a+b)
    return(a+b)
    
result = Button2(50,50)
print(result)
'''
#share another file code using import:
'''
import Loops #or import Loops as Lop <- you can use this

Loops.Button() #content comes here from Loops file
#partial Loading(import only specific sentences)
#e.g from Loops import Button1,Button2

#OR
# import Loops *   #<-import all functions

'''
#import and pip install 
'''
import os
import time 
#print(dir(os))

import requests
#print(dir(requests))
import jupyter_requests 
print(dir(jupyter_requests))
'''




    
    


 

