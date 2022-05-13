l1=['adi', 'maddy', 'ananya', 'adi']
l2=['apple', 'ms','amazon', 'apple']

ziplist= list(zip(l1,l2))
zipset= set(zip(l1,l2))
zipdict= dict(zip(l1,l2))

print(ziplist)
print(zipset)
print(zipdict)
