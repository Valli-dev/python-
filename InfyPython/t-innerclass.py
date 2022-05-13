class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.lap = self.Laptop()

    def show(self):
        print( "Name= {}, age ={}".format(self.name, self.age))
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.name= "HP"
            self.cpu="i5"

        def show(self):
            print(self.name, self.cpu)

s1= Student("Navin", 30)
s2= Student("Vani", 25)

s1.lap.cpu= "AMD"
lap2 = Student.Laptop()
s1.show()
s2.show()

#s1.lap.cpu
lap3=s1.lap
lap4=s2.lap
print(id(lap3))
print(id(lap4))

print(90/30)
print(35//7)