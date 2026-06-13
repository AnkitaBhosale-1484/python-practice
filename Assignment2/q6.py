"""Write a program that accepts two numbers from user and prints their:
Addition
Subtraction
Multiplication
Division"""

a=int(input("enter the value of a"))
b=int(input("enter the value of b"))

def add(a,b):
    return a+b
print("the sum of a and b is",add(a,b))


def sub(a,b):
    return a-b
print("the sub of a and b",sub(a,b))

def mul(a,b):
    return a*b
print("the mul of a and b",mul(a,b))

def div(a,b):
       return a/b
print("the div of a and b",div(a,b))

"""output...

enter the value of a5
enter the value of b4
the sum of a and b is 9
the sub of a and b 1
the mul of a and b 20
the div of a and b 1.25

"""


