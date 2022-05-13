def remove_duplicates(value):
    #start writing your code here
    s=""
    count=0
    for i in value:
        if i not in s:
            s= s+i 
    #print (s)
    return s



print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))