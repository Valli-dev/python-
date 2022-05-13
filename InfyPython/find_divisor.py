# def find_factors(num):
#     #Accepts a number and returns the list of all the factors of a given number
#     factors = []
#     for i in range(1,(num+1)):
#         if(num%i==0):
#             factors.append(i)
#     return factors

# def find_smallest_number(num):
#     i=int(1)
#     while(True):
#         x=find_factors(i)
#         if(len(x)==num):
#             print(x)
#             break
#         else:
#             i=i+int(1)
#     return x[-1]
#     #start writing your code here

# num=16
# print("The number of divisors :",num)
# result=find_smallest_number(num)
# print("The smallest number having",num," divisors:",result)

def num_factors(n):
	factors=0
	for i in range(1,n+1):
		if n%i==0:
			factors+=1
	return factors


def find_smallest_number(num):
    n=1
    while(True):
        no_of_factors=num_factors(n)
        if no_of_factors==num:
            return n
        else:
            n+=1

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
