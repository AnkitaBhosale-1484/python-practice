#Write a program which accepts one number and checks whether it is perfect number or not.

def checkPerfect(number):
    sum = 0

    for i in range(1, number):
        if number % i == 0:
            sum = sum + i

    if sum == number:
        return True
    else:
        return False


def main():
    value = int(input("Enter the number: "))

    Ans = checkPerfect(value)

    if Ans == True:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


if __name__ == "__main__":
    main()