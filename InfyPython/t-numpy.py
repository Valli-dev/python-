#6 ways of arrays
from numpy import *
a=array([1,2,3,4])
arr = array([1,2,4,4,6], float)
print(a)
print(arr)
print(arr.dtype)

linspace_array = linspace(0,16,10)
b= linspace(1,5,10)
print(linspace_array)
print(b)

print("##############################")

c=logspace(10,40,10)
print(c)
print('%.2f' %c[1])

d=zeros(5)
print(d)

f=ones(10)
print(f)

print( """
10 There's something going on here.
11 With the three double- quotes.
12 We'll be able to type as much as we like.
13 Even 4 lines if we want, or 5, or 6.
14 """)