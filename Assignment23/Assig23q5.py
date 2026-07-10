'''Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.'''

import multiprocessing
import os

def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return (os.getpid(), No, Fact)

def main():
    Data = [10, 15, 20, 25]

    p = multiprocessing.Pool()

    Result = p.map(Factorial, Data)

    p.close()
    p.join()

    for pid, num, fact in Result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Factorial :", fact)
        print()

if __name__ == "__main__":
    main()