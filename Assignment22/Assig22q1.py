#write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

import multiprocessing

def SumSquares(No):
    sum=0
    for i in range(1,No+1):
        sum=sum+(i*i)
    return sum
    
def main():
    size=int(input("enter the list size:"))
    Data=[]
    for i in range(size):
        No=int(input("enter the element"))
        Data.append(No)
    print("list is:",Data)

    p=multiprocessing.Pool()

    Result=p.map(SumSquares,Data)

    print("sum of squares every element in the list",Result)
    p.close()
    p.join()

if __name__=="__main__":
    main()


