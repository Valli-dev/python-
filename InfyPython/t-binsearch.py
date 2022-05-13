pos =0
n=[20, 90,5,67,34,78,23,21,12,10]
s=int(input("Enter number to search list: "))
# def binsearch(lis, s):
#      newlis = sorted(lis)
#      print(newlis)
#      mid = int(len(newlis)/2)
#      if s<=newlis[mid]:
#          for i in range(0,mid+1):
#             if newlis[i] ==s:
#                 globals()['pos']= i
#                 return True
#      elif s>=newlis[mid]:
#          for i in range(mid, len(newlis)+1):
#             if newlis[i] ==s:
#                 globals()['pos']= i
#                 return True
#      else:
#          return False

def binsrch(lis, s):
    newlis= sorted(lis)
    l=0 
    u=len(newlis)-1
    
    while l<= u:
        mid=int((l+u)/2)
        if(newlis[mid] == s):
            globals()['pos']= mid
            return True
        elif( newlis[mid]< s):
            l=mid+1
        elif(newlis[mid]> s):
            u=mid-1
        else:
            return False



if binsrch(n, s):
    print("Number found at position ", pos+1)
else:
    print("Not found")