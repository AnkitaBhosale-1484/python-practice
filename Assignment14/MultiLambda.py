#write a lambda function which accept two numbers and returns multiplicaton

Mul=lambda No1,No2:No1*No2

def main():
    value1=int(input("enter the first number"))
    value2=int(input("enter the second number"))
    Ans=Mul(value1,value2)
    print("multiplication is:",Ans)

if __name__=="__main__":
    main()
