#Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.

def chkGreater(No1,No2):
    if No1>No2:
        return No1
    else:
        return No2
    
def main():
    value1=int(input("enter the first no:"))
    value2=int(input("enter the second no:"))

    Ans=chkGreater(value1,value2)
    print("greater number is:",Ans)

if __name__=="__main__":
    main()
