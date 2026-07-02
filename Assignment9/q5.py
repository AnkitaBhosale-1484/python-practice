#Write a program which accepts one number and checks whether it is divisible by 3 and 5


def cheack(number):
    if number % 3==0 and number % 5==0:
        return True
    else:
        return False
    
def main():
    value=int(input("enter the number:"))
    Ans=cheack(value)
    print("divisible 3 and 5 :",Ans)

if __name__=="__main__":
    main()