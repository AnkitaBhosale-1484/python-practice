#write a program which contains one function named  as Add() which aceepts  two number from user and return addition of that two numbers.

def Add(No1,No2):
    add=No1+No2
    return add

def main():
    value1=int(input("Enter the first number:"))
    value2=int(input("Enter the secound number:"))
    Ans=Add(value1,value2)
    print("Addition is:",Ans)

if __name__=="__main__":
    main()