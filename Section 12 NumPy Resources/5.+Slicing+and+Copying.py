import numpy as np

np.random.seed(0)
np_rand = np.random.random((3,3))

np_sub_rand = np.copy(np_rand[0:3 , 0])
print(np_sub_rand)

np_sub_rand[0] = 1000

print(np_sub_rand)

print(np_rand)