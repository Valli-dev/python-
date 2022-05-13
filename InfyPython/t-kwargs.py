def person(name, **kwargs):
    print("name= ", name)
    print(type(kwargs))
    for i,j in kwargs.items():
        print(i,j)


person("Valli", age="35", city="Seattle", job="python developer")

a=10
b=20

print(int.__add__(a,b))  ##int class with add method taking 2 arguments