class Computer:

    wheels =4   # class variable or static variables common to all objects
    def __init__(self, cpu, ram):

        #self.brand="BMW"
        #self.miles=5
        self.cpu=cpu  #instance variables
        self.ram=ram

    def config(self):
        print("I am i5 16GB computer")
        print("cpu=", self.cpu)
        print("Ram=", self.ram)

#c1= Computer() #invokes constructor and initializes object with values passed in constructor
#c2 = Computer()
#Computer.wheels=5  # change the value of class variable
comp1 = Computer("i3", "16 GB")
comp2= Computer("i5", "1 TB")

comp1.config()  #commonly used object calling method
Computer.config(comp2)  # self is the object paramater
