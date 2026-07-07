#write a program which accept N numbers fromuser and store it into list return MiniMum number from that list 

def Minimum(Data):

    for i in Data:

        Min=Data[0]
        for i in Data:
            if i<Min:
                Min=i

    return Min
    


def main():
    size=int(input("enter the size:"))
    print("enter the list:")
    Data=[]
    for i in range(size):
        No=int(input())
        Data.append(No)


    
    Ans=Minimum(Data)
    print("Minimum number is:",Ans)
   



if __name__=="__main__":

    main()