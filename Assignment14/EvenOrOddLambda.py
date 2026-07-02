#write a lambda function  which accept one number and returns True if number is even otherwise False
EvenOdd=lambda No1:True if No1%2 ==0 else False

def main():
    value=int(input("enter the number"))
    Ans=EvenOdd(value)
    print("Even or Odd",Ans)


if __name__=="__main__":
    main()