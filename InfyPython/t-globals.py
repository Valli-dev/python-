a=10
print(id(a))

def func():
    #global a
    a=20
    print("Inside the func: local value of a =", a)
    x= globals()['a']
    print(id(x))
    print(x)
    # a=9
    # print(a)
    globals()['a'] =25
    print(a)
    print(globals()['a'])


func()
print("outside the func :Value of a= ", a)