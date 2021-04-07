import numpy as np

np_arr = np.array([ [1,5,3] , [4, 1 , 6] , [2, 4 , 10]])

np_cond = np_arr[np_arr > 3]
print(np_cond)
print(np_arr > 3)