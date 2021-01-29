#who is faster list or dictionary
secret_key = 9999999

var_list = []

for i in range(1000000):
    var_list.append(i)
    
var_dic = {}

for i in range(10000000):
    var_dic[i] = i
 
#############################################3    
import time 

start = time.time()
for item in var_list:
    if item == secret_key:
        print('Found in List',item)
end = time.time()

print(end-start,"time taken in list")  

start = time.time() 
print('found in dic',var_dic[secret_key])
end = time.time() 

print(end-start,"time taken in Dict")  

#dictionary is lot faster than list



