from numpy import *
arr1 = array([
    [1,2,3],
    [5,6,7],
     [8,9,10]
])
print(arr1)
print(arr1.shape) # prints the  number of rows and columns
print(arr1.dtype) #prints the datatype
print(arr1.ndim)    #prints the dimention ranking of the array
print(arr1.size)    #prints the number of elements in array
arr2= arr1.flatten()# prints multi dimension to 1D array
print(arr2)