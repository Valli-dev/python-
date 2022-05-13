teststring="lw34rtfg899034"
digit=''
for i in range(len(teststring)):
    if teststring[i].isdigit():
        digit=digit+ teststring[i]
        

print(digit)

res= list(filter(lambda x : x.isdigit(),teststring))  # using lambda function
print(''.join(res))

def recurringchar(input_string):
    newstring=set()
    for i in input_string:
        newstring.add(i)
    return (''.join(newstring))


print(recurringchar('missippi'))