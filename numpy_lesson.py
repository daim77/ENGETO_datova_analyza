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

# # ===== generuj pole 1D o delce 1 mio s normalnim rozdelenim a over pravidlo 3 sigma =====
# norm_array = np.random.normal(0, 1, 1*1000*1000)
# cond = (norm_array > -3) & (norm_array < 3)
# print(type(cond))
# my_list = list(cond)
# print(my_list.count(True) / 1000000)

# a = np.array([[1, 3, 3], [1, 4, 3], [2, 7, 7]])
# at = a.T
# print(a)
# print(at)  # transpozice
# print(a.diagonal(-1))
# print()
# b = np.linalg.inv(a)
# print(a.dot(b))

# A = np.array([1, 2, 3])
# B = 2
#
# print(A * np.repeat(B, 3))


# A = np.array([[0,  0,  0],
#               [10, 10, 10],
#               [20, 20, 20],
#               [30, 30, 30]])
#
# B = np.array([1, 2, 3])
#
# print(A + B)

# ==== TASK ====

# a_np = np.random.random(size=(5, 3))
# print(a_np)
# print()
#
# b_np = a_np.copy()
# b_np = np.delete(b_np, 1, axis=1)
# print(b_np)
# print()
#
# c_np = np.append(b_np, np.random.randint(1, 10, size=(5, 1)), axis=1)
# print(c_np)
# print()
#
# print(np.concatenate((a_np, c_np), axis=1))
# print(np.concatenate([a_np, c_np], axis=0))

# vektorizace
# arr = np.arange(10)
# new_arr = np.where(arr % 3 == 0, 1, 0)
# print(new_arr)


def my_cond(x):
    if x % 3 == 0:
        return 1
    else:
        return 0


my_vector_func = np.vectorize(my_cond)
np.random.seed(1)
arr = np.random.randint(0, 10, size=(10000, 1000))

# new_arr = np.zeros(arr.shape)
# for i, row in enumerate(arr):
#     for j, val in enumerate(row):
#         if val % 3 == 0:
#             new_arr[i, j] = 1
#         else:
#             new_arr[i, j] = 0
# duration 20s


# new_arr2 = np.where(arr % 3 == 0, 1, 0)
# duration 400 ms !!

my_vector_func(arr)
