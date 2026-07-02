#Write a program which accepts one number and prints sum of first N natural numbers.


def sum_natural(No):
    sum = 0

    for i in range(1, No + 1):
        sum = sum + i

    print("Sum of first", No, "natural numbers is:", sum)

def main():
    value = int(input("Enter a number: "))
    sum_natural(value)

if __name__ == "__main__":
    main()