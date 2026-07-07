#write a program which accept  N number from user and store it into list .return maximum number from the list


def Maximum(Data):

    for i in Data:

        Max=Data[0]
        for i in Data:
            if i>Max:
                Max=i

    return Max
    


def main():
    size=int(input("enter the size:"))
    print("enter the list:")
    Data=[]
    for i in range(size):
        No=int(input())
        Data.append(No)


    
    Ans=Maximum(Data)
    print("Maximum number is:",Ans)
   



if __name__=="__main__":

    main()