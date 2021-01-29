# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:54:51 2021

@author: siddh
"""

#Dictionary

#key : value

#dic = {'key1' : 'value','key2' : [12,'value2']} #eachkey and value is one item 

dic = {'google_account'     : 'asaksaskajshaksak#4sdj',
       'facebook_account'   : '#23jsjsfhkdhk45kbckc',
       'bank_account'       : ['nsksnfkafqib231',123,456]}


'''
#this print value that you give in input

key = input('enter the acc')
print('This is your password',dic[key])

'''

'''
print(dic['google_account'])
print(dic['bank_account']) #multiple values

'''





# see pyperclip on google(cpoy paste)

#see what we can do with dictionary

#print(dir(dic))

#print(dic)

#print(dic.items())

#print(dic.values()) #just print values not key
'''
print(dic.pop('facebook_account')) #delete
print(dic)
'''
#print data from dictionary
'''
print(dic.get('bank_account'))

print(dic['google_account'])
'''
#dic.popitem() #show you deleted item

## If key is missing

#print(dic['fb']) #by this get method chance to crash program
'''
print(dic.get('fb','key is missing')) #key fb is not in dic 

#or

var = 'key is missing using var'
print(dic.get('fb',var))
'''

list = ['1','45','hello']

print('*#*'.join(list))

print('\n *'.join(list)) #first not get * cause 








