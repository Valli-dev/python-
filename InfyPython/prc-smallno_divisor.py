def find_smallest_number(num):
    div=0
    #start writing your code here
    for i in range(1,num+1):
        if num%i==0:
            div += 1

    return div        


num=16
number=1

print("The number of divisors :",num)
while(True):
   
    result=find_smallest_number(number)
    if result==num:
        break
    number+=1
#result=find_smallest_number(num)
print("The smallest number having",num," divisors:",number)