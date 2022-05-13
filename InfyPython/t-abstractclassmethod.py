#abstract method by default not supported in python, so import the module.
#this abstractmethod has only declaration and min one abstract methods in a class called abstract class 
from abc import ABC , abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Process running")

class Programmer:
    def work(self, com):
        print("Debugs")
        com.process()  #access abstract method in a non abstract class


lap1=Laptop()
lap1.process()
p1=Programmer()
p1.work(lap1)
