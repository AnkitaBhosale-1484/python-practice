#write a program which accept N numbers from user and store it into list return addition of all elements from that list 


def Addition(Data):
    sum=0

    for i in Data:
        sum=sum+i
    return sum


def main():
    size=int(input("enter the size:"))
    print("enter the list:")
    Data=[]
    for i in range(size):
        No=int(input())
        Data.append(No)


    
    Ans= Addition(Data)
    print("addition is:",Ans)
   



if __name__=="__main__":

    main()