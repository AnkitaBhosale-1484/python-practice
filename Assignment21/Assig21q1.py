'''Design a Python application that creates two threads named Prime and NonPrime.

Both threads should accept a list of integers.
The Prime thread should display all prime numbers from the list.
The NonPrime thread should display all non-prime numbers from the list.'''

import threading

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True


def Prime(Data):
    print("Prime Numbers are:")
    for i in Data:
        if ChkPrime(i):
            print(i)


def NonPrime(Data):
    print("Non Prime Numbers are:")
    for i in Data:
        if not ChkPrime(i):
            print(i)


def main():

    size = int(input("Enter size: "))

    Data = []

    print("Enter elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    T1 = threading.Thread(target=Prime, args=(Data,))
    T2 = threading.Thread(target=NonPrime, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()