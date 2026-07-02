#write lambda function using reduce () which accepts  list of number and returns minimum elements
from functools import reduce

Minimum = lambda Data: reduce(lambda No1, No2: No1 if No1 < No2 else No2, Data)

def main():
    value = list(map(int, input("Enter the list: ").split()))

    Ans = Minimum(value)
    print("Minimum element is:", Ans)

if __name__ == "__main__":
    main()