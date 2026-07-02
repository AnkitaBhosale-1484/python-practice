#Write a program which accepts one number and prints all even numbers till that number

def evenNumbers(number):
    for i in range(2, number + 1, 2):
        print(i)

def main():
    value = int(input("Enter a number: "))
    evenNumbers(value)

if __name__ == "__main__":
    main()