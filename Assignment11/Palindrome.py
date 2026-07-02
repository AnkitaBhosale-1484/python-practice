#Write a program which accepts one number and checks whether it is palindrome or not


def checkPalindrome(number):
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    if original == reverse:
        return True
    else:
        return False


def main():
    value = int(input("Enter the number: "))

    Ans = checkPalindrome(value)

    if Ans == True:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")


if __name__ == "__main__":
    main()