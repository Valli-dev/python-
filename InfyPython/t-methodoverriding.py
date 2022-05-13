#method overloading not supported in python. 
# one method name with different  number of parameters 
# is method overloading in same class


#two methods with same name and same parameters in different classes
# is method overriding

print("!!!!!!!!!!!! Method overloading indirect way !!!!!!!!!!!")
class Student:
    def __init__(self, m1, m2):
        self.m1= m1
        self.m2= m2
    
    def sum(self,m1=None,m2=None, m3=None):
        if m1 !=None and m2 !=None and m3 !=None:
            s=m1+m2+m3
        elif m1 !=None and m2 !=None:
            s=m1+m2
        else:
            s=m1
        return s

    def __str__(self):
        return "{} {}".format(self.m1,self.m2)

s1= Student(70,50)
print(s1)
print(s1.sum(50,90,80))  #method overloading indirect way
print(s1.sum(20,90))
print(s1.sum(20))

print("!!!!!!!!!!!! Method overriding  !!!!!!!!!!!")

class A:
    def show(self):
        print("I am from A")

class B(A):
    #pass
    def show(self):
        print("I am from B")

#a = A()
b= B()
#a.show()
b.show()