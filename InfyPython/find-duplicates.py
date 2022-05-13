# def find_duplicates(list_of_numbers):
#     #s=set()
#     list_of_duplicates=[]
#     #print(s)
#     for i in range(len(list_of_numbers)):
#         count=0
#         for j in range(i+1, len(list_of_numbers)):
#             if list_of_numbers[i] ==list_of_numbers[j]:
#                 count += 1
#                 if count ==1 and list_of_numbers[j] not in list_of_duplicates:
#                     list_of_duplicates.append(list_of_numbers[j])
#                 else:
#                     break
#     return list_of_duplicates
#     #start writing your code here

# list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
# list_of_duplicates=find_duplicates(list_of_numbers)
# print(list_of_duplicates)

def find_duplicates(list_of_numbers):
    l=[]
    for i in list_of_numbers:
        x=list_of_numbers.count(i)
        print(x)
        if x>=2:
            l.append(i)
            l=set(l)
            l=list(l)
    return l

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)

l1=[1,2,2,3,3,3,4,4,4,4]
s= set(x for x in l1 if l1.count(x)>1)
print(s)

l1=[1,2,2,3,3,3,4,4,4,4]
l2=[]
for i in l1:
    if l1.count(i)>1:
        l2.append(i)
print(set(l2))


