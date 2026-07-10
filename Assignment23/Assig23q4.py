
'''Write a program that counts how many odd numbers exist between 1 and N using Pool.map().'''

import multiprocessing
import os

def CountOdd(No):
    Count = 0

    for i in range(1, No + 1):
        if i % 2 != 0:
            Count = Count + 1

    return (os.getpid(), No, Count)

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = multiprocessing.Pool()

    Result = p.map(CountOdd, Data)

    p.close()
    p.join()

    for pid, num, count in Result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Odd Number Count :", count)
        print()

if __name__ == "__main__":
    main()