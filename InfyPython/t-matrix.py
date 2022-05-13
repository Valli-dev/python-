from numpy import *
a= array([1,2,3])
b= a.view()
print(b)
print(id(a))
print(id(b))
b[2]=90
print(b)
print(a)

arr1 = array ([
    [1,2,3,4,5,6],
    [7,8,9,0,1,3]
])
arr3 = arr1.flatten()
print(arr3)
arr2 =arr1.reshape(3,4)
print(arr2)
print("--------------------")
m=matrix(arr1)  #convert array into matrix
print(m)
mstr= matrix('10 20 30; 40 50 60; 70 80 90') #matrix input 

mstr2= matrix('1 2 3; 4 5 6; 7 8 9')
print(mstr)

mdiag=mstr.diagonal()
print(mdiag)
print(mstr.min())
print(mstr.max())

mstr3 = mstr +mstr2
print(mstr3)

mstr4= mstr * mstr2 
print(mstr4)