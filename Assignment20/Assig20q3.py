#design python application that creats two threads namedEvenList and OddList
#both threads should accept a list if integers as input 
#the evenlist thread should 
#extract all even elements from the list
#calculate and display their sum
#the oddlist thread should
#extract all odd elements from the list 
#calculate and display their sum
#Threads should run concurrently

import threading

def EvenList(Data):
    Sum = 0
    for i in Data:
        if i % 2 == 0:
            print("Even Thread :", i)
            Sum += i
    print("Even Sum :", Sum)


def OddList(Data):
    Sum = 0
    for i in Data:
        if i % 2 != 0:
            print("Odd Thread :", i)
            Sum += i
    print("Odd Sum :", Sum)


def main():

    size = int(input("Enter the size of list: "))

    Data = []

    print("Enter the elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    T1 = threading.Thread(target=EvenList, args=(Data,))
    T2 = threading.Thread(target=OddList, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()