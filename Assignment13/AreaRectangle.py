#Write a program which accepts length and width of rectangle and prints area.

def rectangleArea(length, width):
    area = length * width
    return area


def main():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    Ans = rectangleArea(length, width)

    print("Area of Rectangle is:", Ans)


if __name__ == "__main__":
    main()