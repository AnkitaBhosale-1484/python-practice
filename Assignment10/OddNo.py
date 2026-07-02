#Write a program which accepts one number and prints all odd numbers till that number

def oddNumbers(number):
    for i in range(1, number + 1, 2):
        print(i)

def main():
    value = int(input("Enter a number: "))
    oddNumbers(value)

if __name__ == "__main__":
    main()