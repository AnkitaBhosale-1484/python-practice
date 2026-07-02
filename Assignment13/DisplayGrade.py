#Write a program which accepts marks and displays grade.


def displayGrade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"


def main():
    value = int(input("Enter the marks: "))

    Ans = displayGrade(value)

    print("Grade:", Ans)


if __name__ == "__main__":
    main()