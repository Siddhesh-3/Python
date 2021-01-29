# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 13:58:05 2021

@author: siddh
"""
#boolean

# True T
#False F

#list And Tuples

#List (Mutable you )

#list = [1,2,3,4,'Hello',15.5,True] #mixed container


#print(list)
#print(list[4]) #print 4th value
#print(list[-2]) #last second value\
  
#add item to list    
'''    
list.append(300) 
print(list)   

'''

#insert specific location
'''
list.insert(2,'second ')  
print(list)

'''
#remove at the end (stack) *last in first out
'''
list.pop()
print(list)
'''
#remove particular item
'''
list.remove(2)
print(list)

'''
#length and count
'''
print(len(list))

print(list.count(55)) #find the string or number you pass in count
'''
#reverse list 
'''
list.reverse() #or list[::-1] 
print(list)

'''
#Sorting 

#number sort

'''
list2 =[5,4,6,15,50,100,2] # sort not support  mixed datatype
list2.sort()

print(list2)
'''
#string sort
'''
list3=['hello','zero','asole']
list3.sort()
print(list3)
'''

#..........................................................

#Tuple (immutable you cant add,update and delete)

newlist = [12,45,4545,845,446,'fdgdfgdg',15.5,True]

#print(type(newlist))

tuple = (12,45,4545,845,446,'fdgdfgdg',15.5,True)

#print(type(tuple))

'''
print(dir(newlist)) #attributes and functions i.e count  #you can add pop modify

print(dir(tuple)) #you cant add update that's why tuple is immutable

print(tuple.__sizeof__()) #size of object 
#in tuple you can use only count and index in tuple

'''
# C is faster than python but Python is easy :)

#str is immutable
'''
a = '12340'
print(a[3])
#but
#a[3] = 2 #not support

list[5] = False
print(list) #support in list add False at position 5

'''
# In list you can update delete 
'''
string = 'aabbcc'

print(string.replace('a','$')) #replace string still inmmutable 

print(string) #your string is still same
'''
#how change tuple value for temp use
'''
tuple = (1,5,8,55)
print(tuple)
print(list(tuple))
 #can convert tuple into list for tempprory use
list(tuple)

print(tuple) #still it has original value

'''
#remove space between string using repalce

'''
string = '    aa  bb aa as '

print(string.replace('','')) #remove spaces

print(string.lstrip('')) #remove left spaces 

print(string.rstrip('')) #remove right spaces 

print(string.strip('aa'))

'''






