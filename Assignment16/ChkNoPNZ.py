#write a program which accept number from user and cheack wheather that number is positive or negative  or zero

def ChkNo(No):
    if (No>0):
        print(f"number is positive:{No}")
    elif (No<0):
        print(f"number is negative:{No}")

    else:
        print(f"number is zero:{No}")



def main():
    value=int(input("enter the number "))
    ChkNo(value)
    

if __name__=="__main__":
    main()