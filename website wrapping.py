# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:36:05 2021

@author: siddh
"""

import requests

content = requests.get('https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI')
complete = (content.text)

listofItem = complete.split('<td id="RI_lastPrice">')

firstsplit = listofItem[1]
      
result = (firstsplit.split('<')[0])


from win10toast import ToastNotifier 
n = ToastNotifier()


n.show_toast("Reliance Stock Price !! ",result,duration = 20)



#<div style="backface-visibility: hidden; transform: translate3d(0px, -845px, 0px); transition: all 0ms ease-in-out 0s;">, . - + 0 1 2 3 4 5 6 7 8 9</div>   