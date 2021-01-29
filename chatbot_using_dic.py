# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:34:46 2021

@author: siddh
"""

dic2 = {'how are you ?' : 'im fine whats about you ',
        'order status' :'please give id',
        'thank you !' : 'Welcome'}
print('Hey Welcome Im simple chat bot having following questions')
print('\n'.join(dic2.keys()))
userinput = input('Enter your Question:')
print('->',dic2[userinput]) 

#Looping - continoous chat
#text input
#text output
#audio input :audio output
# gui 
