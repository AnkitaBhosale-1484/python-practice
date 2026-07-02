#Write a program which accepts one number and prints sum of digits.


def SumDigits(No):
    sum = 0

    while No > 0:
        digit = No % 10
        sum = sum + digit
        No = No// 10

    return sum


def main():
    value = int(input("Enter the number: "))

    Ans = SumDigits(value)

    print("Sum of digits is:", Ans)


if __name__ == "__main__":
    main()