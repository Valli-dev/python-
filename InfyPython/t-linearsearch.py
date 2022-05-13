lis=[10,20,45,60]
s=int(input("Enter number to search:"))
count=0
# if s in n:
#     print("found")

# else:
#      print("Not found")
def linsearch(lis,n):
    for i in lis:
        if i== n:
            return True
        globals()['count'] += 1
    return False   

        
    

if linsearch(lis,s):
    print("number found at", count+1 )
else :
    print("Number not found")

