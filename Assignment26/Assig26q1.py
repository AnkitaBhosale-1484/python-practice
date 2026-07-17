'''Write a Python program to implement a class named Demo with the following specifications:
The class should contain two instance variables: no1 and no2.
The class should contain one class variable named Value.
Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
Implement two instance methods:
Fun() - displays the values of instance variables no1 and no2.
Gun() - displays the values of instance variables no1 and no2.
Create two objects of the Demo class as follows:
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)
Call the instance methods in the given sequence:
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()'''

class Demo:
    value=10


    #constructor
    def __init__(self,A,B):
        self.no1=A
        self.no2=B

     #instance variable
    def fun(self):
        print("inside the fun()")
        print("no1",self.no1)
        print("no2",self.no2)


    #instance variable
    def gun(self):
        print("inside the gun()")
        print("no1",self.no1)
        print("no2",self.no2)

#create class object
obj1=Demo(11,21)
obj2=Demo(51,101)

#call instance
obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()



