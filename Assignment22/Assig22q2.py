'''write a program that calculates factorial of multiple numbers simultaneously using Pool.mao() display process id input number factorial '''

import multiprocessing
import os

def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return (os.getpid(), No, Fact)

def main():
    size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    print("Input List:", Data)

    p = multiprocessing.Pool()

    Result = p.map(Factorial, Data)

    p.close()
    p.join()

    print("\nResult:")
    for pid, num, fact in Result:
        print("Process ID:", pid, "Input:", num, "Factorial:", fact)

if __name__ == "__main__":
    main()