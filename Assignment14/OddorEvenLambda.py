#write a function which accept one number and return True if number is odd otherwise false

EvenOdd=lambda No1:True if No1%2 !=0 else False

def main():
    value=int(input("enter the number"))
    Ans=EvenOdd(value)
    print("number is odd return True otherwise False:",Ans)


if __name__=="__main__":
    main()