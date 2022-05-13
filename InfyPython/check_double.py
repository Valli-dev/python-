def check_double(number):
    num=str(number)
    double= number+number
    check_digits= set(num)
    check_doubledigits=set(str(double))
    #print(check_doubledigits)
    #print(check_digits)
    #print(check_digits.difference(check_doubledigits))
    if check_digits.difference(check_doubledigits) == set():
        return True
    else:
         return False
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(125874))