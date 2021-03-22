import numpy as np

np_arr = np.array([[1,2], [6,8]])
print(np_arr)

np_arr_insert = np.insert(arr = np_arr , obj = 1 , values = [3,4] , axis = 0 )
print(np_arr_insert)

np_arr_append = np.append(arr = np_arr , values = [[3,4], [1,2]])
print(np_arr_append)

np_arr_delete = np.delete(arr = np_arr , obj = 1 , axis = 1)
print(np_arr_delete)

import numpy as np
np_arr= np.array( [[1,2,3], [2,3,5], [1,3,5]] )
np_condarr = np_arr [ np_arr>2 ]
print( np_condarr )
print((np_arr>2).dtype )
