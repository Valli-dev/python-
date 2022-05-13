#accessor methods and mutator methods
#instance methods, class methods and static methods

class Student:
    school="Telusko"

    def __init__(self, m1, m2, m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):    # instance methods
        return (self.m1+ self.m2+ self.m3)/3

    def get_m1(self): #accessor methods
        return self.m1

    def set_m1(self, value): #mutator methods
        self.m1 = value

    @classmethod
    def getschool(cls): # class method, so cls  and no self
        return cls.school


    @staticmethod  # not related to class or object or any variable
    def staticinfo():
        print("This is student class static method")
        print("I dont take cls or self")


s1=Student(35,50,70)

s2=Student(60,70,90)

print(s1.avg())

print(s2.avg())

print(s1.m1)  #accessor method or

#print(s1.get_m1()) 
s1.set_m1(78)
print(s1.m1) 

print(Student.getschool())  # class method called with class name
Student.staticinfo()