#write a lambda function which accept two numbers and returns maximum number

Max=lambda No1,No2: No1 if No1>No2 else No2

def main():
    value1=int(input("enter the first number"))
    value2=int(input("enter the secound number"))
    Ans=Max(value1,value2)
    print("maximum number is",Ans)

if __name__=="__main__":
    main()
