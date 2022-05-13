def add(a,*b):
    x=a
    print("a", a)
    print("b" ,b)
    for i in b:
        x=x+i

    print(x)


add(10)