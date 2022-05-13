l=[9,3,4,5,6,1,2,3,4]
search=3

def binsearch(l, s):
    lower=0
    upper=len(l)
    print(sorted(l))
    l=sorted(l)
    while lower <= upper:
        mid=int(lower+upper/2)
        if s<l[mid]:
            upper=mid
            
        elif s>l[mid]:
            lower=mid
            
        elif s==l[mid]:
            print(s, "found at", mid)
            break
        else: 
            break


binsearch(l, search)