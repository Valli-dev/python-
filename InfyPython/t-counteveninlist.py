def count(l):
    even, odd =0, 0
    print(len(l))
    for i in l:
        if i%2 ==0:
            even +=1
        else:
            odd+=1

    return even, odd

def spellcount(namelist):
    newlist =[]
    #s=set(name)

    for i in namelist:
        if len(i)>5:
            print(i)
            newlist.append(i)
        
    return newlist
    #print(type(s))
    #print(s)


data=[10,5,2,4,6,7,9,0]
even, odd = count(data)
print( "Even ={}, odd= {}".format(even, odd))
#name ="swayam"
namelist = ["swetha", "swapna", "sulthana", "Ashok", "Bhavan", "Navin"]
print(spellcount(namelist))