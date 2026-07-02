#Write a program which accepts radius of circle and prints area of circle.

def circleArea(radius):
    area = 3.14 * radius * radius
    return area


def main():
    radius = float(input("Enter the radius: "))

    Ans = circleArea(radius)

    print("Area of Circle is:", Ans)


if __name__ == "__main__":
    main()