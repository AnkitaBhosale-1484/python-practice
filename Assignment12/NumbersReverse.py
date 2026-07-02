#Write a program which accepts one number and prints that many numbers in reverse

def printReverse(number):
    for i in range(number, 0, -1):
        print(i)


def main():
    value = int(input("Enter the number: "))

    printReverse(value)


if __name__ == "__main__":
    main()