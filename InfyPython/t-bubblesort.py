#num=[90,12,45,78,90,23, 2,5,67,100,1,454]
num=[5,3,8,6,7,2]
l=len(num)
print("-------------sort--------------")
for i in range(0,len(num)):
    #j=i+1
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            t=num[i]
            num[i]=num[j]
            num[j] = t

    print(num)
print(num)

num1=[5,3,8,6,7,2]
print("########Bubble sort#########")
for i in range(len(num1)-1,0,-1):
    #j=i+1
    for j in range(i):
        if num1[j]>num1[j+1]:
            t=num1[j]
            num1[j]=num1[j+1]
            num1[j+1] = t
    print(num1)
print(num1)

num2=[5,3,8,6,7,2]
print("########Selection Sort#########")
for i in range(5):
    minpos=i
    for j in range(i,6):
        if num2[j]< num2[minpos]:
            minpos=j
    temp=num2[i]
    num2[i]=num2[minpos]
    num2[minpos]=temp

    print(num2)

print(num2)