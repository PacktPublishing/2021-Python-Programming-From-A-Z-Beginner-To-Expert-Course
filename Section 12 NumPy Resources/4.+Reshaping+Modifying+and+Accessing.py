import numpy as np

my_arr = np.arange(20)
print(my_arr)

my_arr_reshaped = np.reshape(my_arr , (5,4) , order = "F" ) 
print(my_arr_reshaped)


my_list = list(my_arr)
my_list[1] = 5
my_arr[1] = 6
print(my_list[1])
print(my_arr[1])

my_list_reshaped = list(my_arr_reshaped)
print(my_arr_reshaped[0,1])
print(my_list_reshaped[0][1])