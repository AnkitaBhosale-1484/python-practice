'''Write a Python program to implement a class named Arithmetic with the following characteristics:

The class should contain two instance variables: Value1 and Value2.
Define a constructor (__init__) that initializes all instance variables to 0.
Implement the following instance methods:
Accept() -accepts values for Value1 and Value2 from the user.
Addition() -returns the addition of Value1 and Value2.
Subtraction() -returns the subtraction of Value1 and Value2.
Multiplication() -returns the multiplication of Value1 and Value2.
Division() -returns the division of Value1 and Value2 (handle division by zero properly).
Create multiple objects of the Arithmetic class and invoke all the instance methods for each object.'''

class Arithmetic:

    # Constructor
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    # Accept values from user
    def Accept(self):
        self.Value1 = int(input("Enter first number: "))
        self.Value2 = int(input("Enter second number: "))

    # Addition
    def Addition(self):
        return self.Value1 + self.Value2

    # Subtraction
    def Subtraction(self):
        return self.Value1 - self.Value2

    # Multiplication
    def Multiplication(self):
        return self.Value1 * self.Value2

    # Division
    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not possible"
        else:
            return self.Value1 / self.Value2

    # Display results
    def Display(self):
        print("Value1 :", self.Value1)
        print("Value2 :", self.Value2)
        print("Addition :", self.Addition())
        print("Subtraction :", self.Subtraction())
        print("Multiplication :", self.Multiplication())
        print("Division :", self.Division())


def main():

    print("----- Object 1 -----")
    obj1 = Arithmetic()
    obj1.Accept()
    obj1.Display()

    print("\n----- Object 2 -----")
    obj2 = Arithmetic()
    obj2.Accept()
    obj2.Display()


if __name__ == "__main__":
    main()