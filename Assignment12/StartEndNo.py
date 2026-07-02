#Write a program which accepts one number and prints that many numbers starting from 1.

def printNumbers(number):
    for i in range(1, number + 1):
        print(i)


def main():
    value = int(input("Enter the number: "))

    printNumbers(value)


if __name__ == "__main__":
    main()