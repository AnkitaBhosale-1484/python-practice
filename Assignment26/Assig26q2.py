'''Write a Python program to implement a class named Circle with the following requirements:
The class should contain three instance variables: Radius, Area, and Circumference.
The class should contain one class variable named PI, initialized to 3.14.
Define a constructor (__init__) that initializes all instance variables to 0.0.
Implement the following instance methods:
Accept() - accepts the radius of the circle from the user.
CalculateArea() -calculates the area of the circle and stores it in the Area variable.
CalculateCircumference()-calculates the circumference of the circle and stores it in the Circumference variable.
Display()-displays the values of Radius, Area, and Circumference.'''

class Circle:
    # Class Variable
    PI = 3.14

    # Constructor
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # Accept radius from user
    def Accept(self):
        self.Radius = float(input("Enter the radius: "))

    # Calculate area
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    # Calculate circumference
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    # Display details
    def Display(self):
        print("Radius :", self.Radius)
        print("Area :", self.Area)
        print("Circumference :", self.Circumference)


def main():
    obj = Circle()

    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()


if __name__ == "__main__":
    main()