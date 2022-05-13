list=[1,2,3,2,3,4,1,5,6] 
output={1:2, 2:2 , 3:2, 4:1, 5:1, 6:1}
for num in list:
    print("Number is", num,list.count(num))
key1=set(list)
dict={}
val=[]
for i in list:
    print(i)
    val.append(list.count(i))
print(val)

for key in key1:
    for value  in val:
    
            dict[key]= value
            val.remove(value)
            break

print(str(dict))
