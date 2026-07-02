#Write a program which accepts one number and prints reverse of that number.

def ReverseNo(number):
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return reverse


def main():
    value = int(input("Enter the number: "))

    Ans = ReverseNo(value)

    print("Reverse number is:", Ans)


if __name__ == "__main__":
    main()