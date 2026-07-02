#write lambda function using reduce () which accepts  list of number and returns the addition of  all elements

from functools import reduce

Addition = lambda Data: reduce(lambda No1, No2: No1 + No2, Data)

def main():
    value = list(map(int, input("Enter the list: ").split()))

    Ans = Addition(value)
    print("Addition of all elements is:", Ans)

if __name__ == "__main__":
    main()