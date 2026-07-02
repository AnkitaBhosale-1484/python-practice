#Write a program which accepts one number and prints count of digits in that number.

def CountDigits(No):
    count = 0

    while No > 0:
        No = No// 10
        count = count + 1

    return count


def main():
    value = int(input("Enter the number: "))

    Ans = CountDigits(value)

    print("Count of digits is:", Ans)


if __name__ == "__main__":
    main()