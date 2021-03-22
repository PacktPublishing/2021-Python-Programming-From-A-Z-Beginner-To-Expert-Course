import numpy as np

np_arr = np.array([[2,3], [4,10]])
np_arr_broad = np_arr *5

np_five = np.array([[5,5], [5,5]])
np_arr_nobroad = np_arr*np_five
print(np_arr_nobroad)