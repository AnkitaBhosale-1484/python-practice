def multiplication(NO1,NO2):
    ANS=NO1*NO2
    return ANS


def main():
    print("enter the first number")
    NO1=int(input())

    print("enter the secound number")
    NO2=int(input())

    Ret=multiplication(NO1,NO2)
    print(Ret)


if __name__=="__main__":
        main()