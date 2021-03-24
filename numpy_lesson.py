import numpy as np


# my_array = np.zeros(3, dtype='int8')
# print(my_array)
# print(type(my_array))
# print(np.zeros(3))
# print(np.ones(4).reshape(4,1))
# print(np.random.random(5)) # randint, .uniform, .normal
# print(np.random.normal(5, 1, size=(3, 2)))
# ma = np.random.uniform(1, 10, 1)
# print(np.random.choice(ma))

# ma = np.random.randint(1, 20, (2, 3, 4))
# print(ma)
# print()
# # print(ma[1, :2, 0])
# cond = ma > 4
# print(cond)
# print(ma[cond])

# array_a = np.array([1, 2, 3])
# array_b = np.array([7, 8, 9])
# print(array_a + array_b)
# print(array_a - array_b)
# print(array_a * array_b)
# print(array_a.sum())  # mean, max, min atc

# arr_c = np.array([[1, 2, 3], [7, 8, 9]])
# print(arr_c)
# print(arr_c.sum(axis=1))

# generuj pole 1D o delce 1 mio s normalnim rozdelenim a over pravidlo 3 sigma
norm_array = np.random.normal(0, 1, 1*1000*1000)
cond = (norm_array > -1) & (norm_array < 1)
my_list = list(cond)
print(my_list.count(True) / 1000000)
