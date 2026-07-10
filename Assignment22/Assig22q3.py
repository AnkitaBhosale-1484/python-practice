'''for every number in the given list,count how many prime numbers exist between 1 and N using multiprocessing pool
'''

import multiprocessing

def CountPrime(No):
    Count = 0

    for i in range(2, No + 1):
        Prime = True

        for j in range(2, i):
            if i % j == 0:
                Prime = False
                break

        if Prime:
            Count = Count + 1

    return (No, Count)

def main():
    size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    print("Input List:", Data)

    p = multiprocessing.Pool()

    Result = p.map(CountPrime, Data)

    p.close()
    p.join()

    print("\nResult:")
    for num, count in Result:
        print("Input:", num, "Prime Count:", count)

if __name__ == "__main__":
    main()