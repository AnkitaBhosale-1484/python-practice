# Write a lambda function using reduce() which accepts a list of numbers
# and returns the product of all elements.

from functools import reduce

Product = lambda Data: reduce(lambda No1, No2: No1 * No2, Data)

def main():
    value = list(map(int, input("Enter the list: ").split()))

    Ans = Product(value)
    print("Product of all elements is:", Ans)

if __name__ == "__main__":
    main()