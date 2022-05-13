#1.compile time error---syntax error, compile time
#2.logical errors---code gets compiled with wrong output
#3.run time error --code throws error while running specific inputs
a=10
b='p'
try:
    print(a/b)

except ZeroDivisionError:
    print("divide by zero error")
    
except:
    print("error")
finally: 
    print("bye")
print("hello ")

