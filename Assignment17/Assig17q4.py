#write a program which accept one number form user and return addition of its factor 

def  AdditionFactor(No):
    sum=0
    for i in range(1,No+1):
        if No%i==0:
            sum=sum+i
    return sum



def main():
    value=int(input("enter the number"))
    Ans=AdditionFactor(value)
    print(Ans)


if __name__=="__main__":
    main()