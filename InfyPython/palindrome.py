def is_palindrome(word):  
    s=str.lower(word)
    # if s == s[::-1]:
    #     return True




    rev= ''.join(reversed(s))
    if s==rev:
        return True




#    print(s)
#    n=(len(word))
#    while n> 0:
#        for i in range(n):
#            if s[i] == s[n-1]:
#                n-=1 
#            else:
#                 return False
#    return True
   
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
#result=is_palindrome("madam")
#result=is_palindrome("kayak")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")