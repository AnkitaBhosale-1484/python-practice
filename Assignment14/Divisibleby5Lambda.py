#write a lambda function which accept one number  and return True if divisible by 5.

Divisible=lambda No1:True if No1%5==0 else False

def main():
    value=int(input("enter the number"))
    Ans=Divisible(value)
    print("return True number is divisible by 5:",Ans)

if __name__=="__main__":
    main()
    