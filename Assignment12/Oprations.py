#Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def arithmeticOperation(no1, no2):
    add= no1 + no2
    sub = no1 - no2
    multi= no1 * no2

    return add, sub, multi


def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    add, sub, mul = arithmeticOperation(value1, value2)

    print("Addition is:", add)
    print("Subtraction is:", sub)
    print("Multiplication is:", mul)


if __name__ == "__main__":
    main()