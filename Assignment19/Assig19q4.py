#write a program which contain filter(),map(),and reduce()in it python application which contains one list of numbers.
# list contains the numbers which are accepted from user filter should filter out all  such numbers  which are even .Map function will calculate its square reduce will return addition of all that number
from functools import reduce

def FilterData(Data):
    return list(filter(lambda x:x%2==0,Data))
def MapData(Data):
    return list(map(lambda x:x*x,Data))

def ReduceData(Data):
    return reduce(lambda x,y:x+y,Data)
    


def main():
    size=int(input("enter the size:"))
    Data=[]
    print("enter the element:")
    for i in range(size):
        Data.append(int(input()))

    print("list",Data)

    FData=FilterData(Data)
    print("even number in the list",FData)

    MData=MapData(FData)
    print("square of even number",MData)

    if len(MData)>0:
        ans=ReduceData(Data)
        print("summation",ans)
    else:
        print("element not found")


if __name__=="__main__":
    main()















