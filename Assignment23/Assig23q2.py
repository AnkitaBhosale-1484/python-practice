'''write  a python program using mutiprocessing.pool to calculate the sum of all odd numbers from  a to N'''


import multiprocessing

def SumOdd(No):
    Sum = 0

    for i in range(1, No + 1, 2):
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

    Result = p.map(SumOdd, Data)

    p.close()
    p.join()

    print("\nResult:")
    for num, total in Result:
        print("Input:", num, "Sum of Odd Numbers:", total)

if __name__ == "__main__":
    main()