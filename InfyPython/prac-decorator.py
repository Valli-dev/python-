class Employee:
    def __init__(self, first, last):
        self.first =first
        self.last= last
        #self.email =self.first + '.'+ self.last + '@gmail.com'
        #self.fullname= self.first + self.last
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first=None
        self.last=None


emp1 = Employee('John','Smith')
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
emp1.first = 'Jim'
print(emp1.email)

print(emp1.fullname)

emp1.fullname = 'Corey Schafer'
print(emp1.first)
print(emp1.last)
print(emp1.email)
del(emp1.fullname)
print(emp1)