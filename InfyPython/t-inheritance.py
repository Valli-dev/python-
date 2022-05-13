#single level inheriance class A: and class B(A):
#multi level inheritance, class A: and class B(A): and class C(B):
#multiple inheritance, class A:, class B:, class c(A,B)
class A:
    def __init__(self):
        print("Constructor init A")
    def feature1(self):
        print("in feature 1")
class B():
     def feature2(self):
        print("in feature 2")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("Constructor init C")
    def feature3(self):
        print("in feature3")

    def feat(self):
        super().feature1()

b1=C()
b1.feat()