from array import *
# a=array([1,1,2,3,4,5])
# b=(a+5)

# arr1 =([1,1,1,1,1,1])
# arr2=arr1

# print(id(arr1))
# print(id(arr2))
# print(arr2)   ##vectorized array
# print(b)
# print(sin(b))

# print(sum(arr2))
# print(sqrt(b))
# print(id(b))
# print(sorted(b))
# print(list(reversed(b)))
# #print(x)
# seq_range = range(5, 9)
# print(list(reversed(seq_range)))

# # for list
# seq_list = [1, 2, 4, 3, 5]
# print(list(reversed(seq_list)))

# c=a+b
# print(c)
# d=concatenate([a,b])
# print(d)

arr1=array('i',[1,2,3,4,5])
#arr2=[6,7,8,9,10]
#arr2=arr1.copy()  #deep copy 

#arr3=arr1.view()  #shallow copy

#arr2[2]=6

# print(arr1)
# print(arr2)


# print(id(arr1))
# print(id(arr2))
# print(id(arr3))
add=array('i', [])
print("add=", add)
arr1=array('i', [1,2,3,4,5])
arr2=array('i', [6,7,8,9,10])
j=0
for i in arr1:
    num3 =i + arr2[j]
    add.append(num3)
    j+=1
print(add)
#j=i+1

add=array('i', [5,2,9,14,8,25,12,90,45])
print(len(add))

for i in range(len(add)-1):
    j=i+1
    if add[i] > add[j]:
        big=add[i]
    
    else:
        big=add[j]
        
print("big number in array is '%d'" %big)