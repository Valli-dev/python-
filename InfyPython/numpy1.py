from ctypes import sizeof
import numpy as np
import sys
l=range(100)
s=[5,10,15]
print(type(l))
print(sys.getsizeof(5)* len(l))
n=[]
print(n.__sizeof__())
print(sys.getsizeof(n))
array = np.arange(100)
print(type(array))
print(array.size * array.itemsize)
