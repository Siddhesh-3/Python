# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:39:57 2021

@author: siddh6
"""

#Conditional Statements  :
    
# Home - Shop - Home

#ifelse inside ifelse called nested statement

#if else statement


# we can use key = 1,2 #for multiple values
#then use if (guess in key):
    
''' 
key = 7
key2 = 0

print('Guess number betn 0-9')

guess = int(input("Enter Your Guess :"))

if (guess == key) or (guess == key2) : #use OR
    print('You won')

# if guess == key or key2 you can use this 
    
elif guess == 6 :
    
    if guess == 6 : #nested ifelse
        print('Try Again !') 
elif guess == 8 :
    print("too close")
else:
    print('lost')
    
'''
    
 #second 
# != not equalto
# ==
#>
#<
#<=
#>=

'''
key = '7'
key2 = '5'
 
guess = input("enter your guess :")
 
if guess == key :
   print("match")
   a = input("enter your second guess :")
   if a == key2:
       print('second matched')
else:
   print("lost")
'''  

# or ,and,not
'''
engine1 = True
engine2 = True #set one of this to False


if engine1 == True and engine2 == True:
    print("full Speed")
elif engine1 == True or engine2 == True:
    print("Half speed")
'''

#Looping/iteration 
#for
#while 
'''
key = 3467

list = [1,23,25,584,987,3467,5485]

#for

for eachitem in list:
  if eachitem == key:
      print(eachitem,"Found the key")
  else:
      print('current item is',eachitem)
      
 #while      
      i = 0
      while i < len(list):
          if list[i] == key:
              print(eachitem,"Found key using while")
          else:
              print('cureent item is',eachitem)
          i = i+1
'''

#Infinite Loop
#e.g
#ATM 

#enter card and pin number
#enter ammount
#get cash 
#thank you
'''
key = 7
i = 0
while True :
    #do something
    guess = int(input("Enter :"))
    if guess == key :
        print("won")
    else:
        print("lost")
    i=i+1   
    '''
#while with condition    
'''
key = 7
i = 0
while i<3 :
    #do something
    guess = int(input("Enter :"))
    if guess == key :
        print("won")
    else:
        print("lost")
    i=i+1    
        '''
#method 3
#case true exit the code
'''
key = 7

status_flag = False
while not status_flag :
    #do something
    guess = int(input("Enter :"))
    if guess == key :
        print("won")
        status_flag = True
    else:
        print("lost")
        
        '''
#Loop Control Statements
#break,continue,pass
'''
key = 7

while True:
    
    guess = int(input("Enter :"))
    if guess == key :
        print("won")
        break  #break
        print("not execute")
    else:
        print("lost")
'''
#continue
'''
key = 7

while True:
    
    guess = int(input("Enter :"))
    if guess == key :
        print("won")
        continue #continue
        print("not execute")
    else:
        print("lost")
'''
#
'''
key = 7

while True:
    
    guess = int(input("Enter :"))
    if guess == key :
        print("won")
        pass #pass
        print("not execute")
    else:
        print("lost")
        
        
'''  


#use this code in 7th lec using import

def Button():
    button =input('Enter button no :')
    print(button)      
   



 





