# Write a program which accepts one number and prints binary equivalent.



def binaryEquivalent(number):
    binary = ""

    while number > 0:
        digit = number % 2
        binary = str(digit) + binary
        number = number // 2

    return binary


def main():
    value = int(input("Enter the number: "))

    Ans = binaryEquivalent(value)

    print("Binary Equivalent is:", Ans)


if __name__ == "__main__":
    main()