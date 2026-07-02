#write a lambda function using map()which accepts a list of numbers and returns a list of squares of each number



Square = lambda Data: list(map(lambda No: No * No, Data))

def main():
    Numbers = list(map(int, input("Enter the numbers: ").split()))

    Ans = Square(Numbers)
    print("Square of each number:", Ans)

if __name__ == "__main__":
    main()