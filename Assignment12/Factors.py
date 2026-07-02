#Write a program which accepts one number and prints its factors.

def printFactors(number):
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)


def main():
    value = int(input("Enter the number: "))

    print("Factors are:")
    printFactors(value)


if __name__ == "__main__":
    main()