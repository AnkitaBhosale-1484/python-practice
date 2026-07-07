#write program which accept number from user and return addition of digits in that numberdef digit(No):
    
def sumdigit(No):
    sum=0
    while(No>0):
        digit=No%10
        sum=sum+digit
        No=No//10
    return sum



def main():
    value=int(input("enter number:"))
    Ans=sumdigit(value)
    print("number of digits:",Ans)



if __name__=="__main__":
    main()