#write a program which contains filter(),map() and reduce() in it .python application which contains one list of number.
# list contains the numbers which are accepted from user .filter should filter out all prime number.map function will multiplay each number by 2.reduce will return maximum number from that numbers(you can also use normal function instead of lambda function)

from functools import reduce

def Prime(No):
    if No<=1:
        return False
    for i in range(2,No):
        if No%i==0:
            return False
        
    return True

def Multiplay(No):
    return No*2
    
def Maximum(No1,No2):
    if No1>No2:
        return No1
    else:
        return No2
        



def main():
    size=int(input("enter the list size:"))
    Data=[]
    
    for i in range(size):
        value=int(input("enter the element:"))
        Data.append(value)

    FData=list(filter(Prime,Data))
    print("Prime No:",FData)

    MData=list(map(Multiplay,FData))
    print("multiplay by 2 of Prime number",MData)

    Ans=reduce(Maximum,MData)
    print("maximum number ",Ans)




if __name__=="__main__":
    main()