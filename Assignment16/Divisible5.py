# write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false

def Divisible(No):
    if (No%5==0):
        return True
    else:
        return False
    


def main():
    value=int(input("enter the number"))
    Ans=Divisible(value)
    print("number is divisible by 5:",Ans)

if __name__=="__main__":
    main()