import numpy as np

my_list = [1,2,3]

my_arr = np.asarray(my_list)
print(my_arr)
print(my_arr.dtype)
print(my_arr.shape)

np_zeros = np.zeros((5,5), dtype = int)
print(np_zeros)

np_ones = np.ones((5,5))
print(np_ones)

np_range = np.arange(start = 2 , step = 2 , stop= 20)
print(np_range)

np_linspace = np.linspace(start = 2 , stop = 20 , num = 5)
print(np_linspace)