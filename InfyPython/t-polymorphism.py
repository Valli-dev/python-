#Duck Typing, # operator overloading #method overloading #method overriding
class Pycharm:
    def execute(self):
        print("compiling")
        print("execution")

class MyEditor:
    def execute(self):
        print("compiling")
        print("execution")
        print("convention check")
        print("spell check")



class Laptop:
    def invoke(self, ide):
        ide.execute()

ide = MyEditor()

L1 = Laptop()
L1.invoke(ide)