'''write a program that calculates 
1^5+2^5+3^5+...+N^5
for multiple vale of N simultaneously using pool.'''

import multiprocessing

def SumPower5(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i ** 5)

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

    Result = p.map(SumPower5, Data)

    p.close()
    p.join()

    print("\nResult:")
    for num, total in Result:
        print("Input:", num, "Sum of 5th Powers:", total)

if __name__ == "__main__":
    main()
    