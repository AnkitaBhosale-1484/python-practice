#write a program which contains one lambda function which accepts two parameters and return its multiplication 

multiplication=lambda No1,No2:No1*No2

def main():
    value1=int(input("enter the first number:"))
    value2=int(input("enter the secound number:"))
    Ans=multiplication(value1,value2)
    print("multiplication is:",Ans)



if __name__=="__main__":
    main()