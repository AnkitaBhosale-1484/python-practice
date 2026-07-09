'''design a python application that creates three threads named small,capital,and digits all threads should  accept a string as input 
the small threads should count and display the number  of lowercase character
the capital thread should count and display the number of uppercase character
the digits thread should count and  display the number of numric digits
each thread must also display threadid threadname'''

import threading

def Small(Str):
    Count = 0

    print("Thread Name :", threading.current_thread().name)
    print("Thread ID   :", threading.get_ident())

    for ch in Str:
        if ch.islower():
            Count = Count + 1

    print("Number of lowercase characters :", Count)


def Capital(Str):
    Count = 0

    print("Thread Name :", threading.current_thread().name)
    print("Thread ID   :", threading.get_ident())

    for ch in Str:
        if ch.isupper():
            Count = Count + 1

    print("Number of uppercase characters :", Count)


def Digits(Str):
    Count = 0

    print("Thread Name :", threading.current_thread().name)
    print("Thread ID   :", threading.get_ident())

    for ch in Str:
        if ch.isdigit():
            Count = Count + 1

    print("Number of digits :", Count)


def main():

    Value = input("Enter a string : ")

    T1 = threading.Thread(target=Small, args=(Value,), name="Small")
    T2 = threading.Thread(target=Capital, args=(Value,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(Value,), name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()