#write a python program using multiprocessing.pool to calculate the sum of all even numbers 1to N for every number from the given list


import multiprocessing

def SumEven(No):
    Sum = 0

    for i in range(2, No + 1, 2):
        Sum = Sum + i

    return (No, Sum)

def main():
    size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    print("Input List:", Data)

    p = multiprocessing.Pool()

    Result = p.map(SumEven, Data)

    p.close()
    p.join()

    print("\nResult:")
    for num, total in Result:
        print("Input:", num, "Sum of Even Numbers:", total)

if __name__ == "__main__":
    main()