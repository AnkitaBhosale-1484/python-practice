'''Write a Python program to implement a class named BankAccount with the following requirements:
The class should contain two instance variables:
Name (Account holder name)
Amount (Account balance)
The class should contain one class variable:
ROI (Rate of Interest), initialized to 10.5
Define a constructor (__init__) that accepts Name and initial Amount.
Implement the following instance methods:
Display() -displays account holder name and current balance.
Deposit() -accepts an amount from the user and adds it to balance.
Withdraw() -accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists).
CalculateInterest() -calculates and returns interest using the formula:
Interest = (Amount * ROI) / 100
Create multiple objects and demonstrate all methods.'''

class BankAccount:

    # Class Variable
    ROI = 10.5

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # Display Details
    def Display(self):
        print("\nAccount Holder :", self.Name)
        print("Current Balance :", self.Amount)

    # Deposit Amount
    def Deposit(self):
        money = float(input("Enter amount to deposit: "))
        self.Amount += money
        print("Amount deposited successfully.")

    # Withdraw Amount
    def Withdraw(self):
        money = float(input("Enter amount to withdraw: "))
        if money <= self.Amount:
            self.Amount -= money
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient Balance.")

    # Calculate Interest
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


def main():

    print("----- Account 1 -----")
    obj1 = BankAccount("Ankita", 10000)
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.Display()
    print("Interest :", obj1.CalculateInterest())

    print("\n----- Account 2 -----")
    obj2 = BankAccount("Rahul", 5000)
    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    obj2.Display()
    print("Interest :", obj2.CalculateInterest())


if __name__ == "__main__":
    main()