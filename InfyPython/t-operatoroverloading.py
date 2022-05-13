a=10
b=20
c='5'
d='6'
print(a+b)
print(c+d)
print(int.__add__(a,b))  ##int class with add method taking 2 arguments
print(int.__sub__(a,b))
print(int.__mul__(a,b)) 
print(str.__add__(c,d)) #magic methods

class Student:
    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1= self.m1 + other.m1
        m2= self.m2 + other.m2
        s3= Student(m1,m2)
        return s3

    def __sub__(self, other):
        m1= self.m1 - other.m1
        m2= self.m2 - other.m2
        s4= Student(m1,m2)
        return s4


    def __gt__(self, other):
        s1= self.m1 + self.m2
        s2= other.m1 + other.m2
        if s1 > s2:
            return s1


    def __str__(self):
        #return self.m1, self.m2  --> return a tuple integer
        return "{} {}".format(self.m1, self.m2) # --> returns in string format

s1= Student(50,80)
s2= Student(80,90)
print("operator overloading : objects added: s3=")
s3= s1+ s2
print(s3)

print("operator overloading : objects subtracted: s4=")
s4=s1-s2
print(s4)
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")


print(s3.m1)
print(s1.__str__())  #printing an object invokes __str__ 

print(s2)  # so def __str__ in class