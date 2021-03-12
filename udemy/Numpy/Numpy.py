import numpy as np

'''
my_list = [1,2,3,4]

my_arr = np.asarray(my_list)
print(my_arr)
print(my_arr.dtype)
print(my_arr.shape)
'''

np_array = np.ones((3,5), dtype  = int)
print(np_array,"\n")

np_range = np.arange(start = 1 , step = 3 , stop = 20)
print(np_range,"\n")

np_range2 = np.linspace(start = 2  , stop = 20 , num = 5)
print(np_range2,"\n")

np_random = np.random.random((2,5))
print(np_random,"\n")

#ex
import numpy as np 
np_arr = np.arange(3 , 10)

#REshapingk