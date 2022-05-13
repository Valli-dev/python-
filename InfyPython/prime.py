#prime number
for num in range(100,200):
    #print("number:",num)
    for i in range(2,num):
        if num%i ==0:
            break
    else:
        print(num)

for num in range(100,200):
    if( all(num%i !=0 for i in range(2,num))):
        print(num)


#0 1 1 2 3 5 8 13 fibanocci
a,b=0,1
n =int(input("Enter number for fibonacci series:"))
if n==0:
    print("fibonacci series: ", 0)
elif n==1:
    print("fibonacci series: ", 1)
else:
    for i in range(0,int(n)):
        c=a+b
        a=b
        b=c
        print(c)

##recursion fibo
def fib(n):
    if n==0:
       return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print("Fibnocci series using recursion:")
for i in range(0,n):
    s=fib(i)
    print(s)



#sorting numbers in list
s=[45,12,34,56,78,21]
s.sort(reverse=True)
print(s)
#print(sorted(s))
s=[45,12,34,56,78,21]
newlist=[]
print("Sorting using manual logic:")
while s:
    min=s[0]
    for x in s:
        if x > min:
            min=x
    newlist.append(min)
    s.remove(min)

print(newlist)


print(newlist[::-1])