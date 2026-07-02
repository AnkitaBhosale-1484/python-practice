# Write a lambda function using filter() which accepts a list of numbers
# and returns the count of even numbers.

CountEven = lambda Data: len(list(filter(lambda No: No % 2 == 0, Data)))

def main():
    value = list(map(int, input("Enter the list: ").split()))

    Ans = CountEven(value)
    print("Count of even numbers is:", Ans)

if __name__ == "__main__":
    main()