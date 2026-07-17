'''Write a Python program to implement a class named Numbers with the following specifications:
The class should contain one instance variable:
Value
Define a constructor (__init__) that accepts a number from the user and initializes Value.
Implement the following instance methods:
ChkPrime() -returns True if the number is prime, otherwise returns False.
ChkPerfect() - returns True if the number is perfect, otherwise returns False.
Factors() -displays all factors of the number.
SumFactors() -returns the sum of all factors.
Create multiple objects and call all methods.'''

class Numbers:

    # Constructor
    def __init__(self, Value):
        self.Value = Value

    # Check Prime
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    # Check Perfect
    def ChkPerfect(self):
        sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i

        if sum == self.Value:
            return True
        else:
            return False

    # Display Factors
    def Factors(self):
        print("Factors are:", end=" ")

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # Sum of Factors
    def SumFactors(self):
        sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum += i

        return sum


def main():

    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    obj1 = Numbers(value1)
    obj2 = Numbers(value2)

    print("\n----- Object 1 -----")
    obj1.Factors()
    print("Prime :", obj1.ChkPrime())
    print("Perfect :", obj1.ChkPerfect())
    print("Sum of Factors :", obj1.SumFactors())

    print("\n----- Object 2 -----")
    obj2.Factors()
    print("Prime :", obj2.ChkPrime())
    print("Perfect :", obj2.ChkPerfect())
    print("Sum of Factors :", obj2.SumFactors())


if __name__ == "__main__":
    main()