'''Design a Python application that creates two threads.

Thread1 should compute the sum of elements from a list.
Thread2 should compute the product of elements from the same list.
Return the results to the main thread and display them.'''

import threading

Sum = 0
Product = 1

def SumList(Data):

    global Sum

    for i in Data:
        Sum = Sum + i


def ProductList(Data):

    global Product

    for i in Data:
        Product = Product * i


def main():

    size = int(input("Enter size: "))

    Data = []

    print("Enter elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    T1 = threading.Thread(target=SumList, args=(Data,))
    T2 = threading.Thread(target=ProductList, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Sum of elements:", Sum)
    print("Product of elements:", Product)


if __name__ == "__main__":
    main()