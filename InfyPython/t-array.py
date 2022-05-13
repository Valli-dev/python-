from array import array as arr
a= arr('i', [])
n = int(input("Enter the array length:"))
for i in range(n):
    x=int(input("Enter the value:"))
    a.append(x)

#print("The values to search : ")
val=int(input("The values to search : "))
j=0

for  i in a:
    if i==val:
        print("Value found in '%d' array :" %j) 
        break

    else:
        j+=1 


print(a.index(val))

b= arr(a.typecode, (x for x in a))
print(b)


