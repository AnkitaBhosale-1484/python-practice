#Write a program which accepts one number and prints factorial of that number


def factorialNo(No):
    fact=1

    for i in range(1,No+1):
        fact=fact*i
    return fact



def main():
    value=int(input("enter the number"))
    Ans=factorialNo(value)
    print("factorial of ",value," is",Ans)

if __name__=="__main__":
    main()