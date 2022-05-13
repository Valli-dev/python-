from threading import *
from time import sleep
import threading

class A(Thread):
    def run(self):
        for i in range(5):
            print("A says Hello")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("B says Hi")
            sleep(1)

a= A()
b= B()

a.start()
sleep(0.2)
b.start()
a.join()
b.join()

print("main thread says bye")


