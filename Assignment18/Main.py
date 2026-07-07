import Num

def ListPrime(Data):
    sum =0
    for i in Data:
        if Num.ChkPrime(i):
            sum=sum+i
    return sum




def main():
    size=int(input("enter the size:"))
    Data=[]
    print("enter the element:")
    for i in range(size):
        No=int(input("enter the number:"))
        Data.append(No)

    Ans=ListPrime(Data)
    print("addition of number is:",Ans)



if __name__=="__main__":
    main()