#write a program which accept one number and display below pattern
def Factorial(No):
    num=1
    for i in range(1,No+1):
        num=num*i
    return num
        

def main():
    value=int(input("enter the number"))
    Ans=Factorial(value)
    print(Ans)


if __name__=="__main__":
    main()