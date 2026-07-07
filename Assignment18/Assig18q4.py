#write a program which accept N number from user and store it into list.accept one another number from user and return frequency of that number from list

def Frequency(Data, No):

    Count = 0

    for i in Data:

        if i == No:
            Count = Count + 1

    return Count





def main():
    size=int(input("enter the list size:"))
    Data=[]
    for i in range(size):
        No=int(input())
        Data.append(No)

    No=int(input("enter the number:"))
    Ans=Frequency(Data,No)
    print("number of frequency is:",Ans)
    
        


if __name__=="__main__":
    main()