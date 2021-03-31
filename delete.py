import collections as cl
from time import time


start = time()
my_list = [str(x) for x in range(100000000)]
# print(my_list)
print(time() - start)

start = time()
my_list.pop()
my_list.append(1000000)
print(time() - start)

qu = cl.deque(my_list)
# print([item for item in qu])
start = time()
qu.pop()
qu.append(1000000)
print(time() - start)

