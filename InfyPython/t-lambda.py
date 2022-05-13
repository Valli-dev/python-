from functools import reduce
marks=[41,51,90,67,78, 35,10,25]

passlist = list(filter((lambda m: m>40), marks))

firstclass= list(map((lambda m: m >60), passlist))
firstclass= list(map((lambda m: m +10 ), passlist))
print(len(passlist), passlist)
print("firstclass: ", firstclass)

sum_marks = reduce((lambda m1,m2: m1+m2), marks)

print(sum_marks)
