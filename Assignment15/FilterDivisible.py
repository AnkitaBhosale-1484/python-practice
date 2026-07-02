# Write a lambda function using filter() which accepts a list of numbers
# and returns a list of numbers divisible by both 3 and 5.

Divisible = lambda Data: list(filter(lambda No: No % 3 == 0 and No % 5 == 0, Data))

def main():
    value = list(map(int, input("Enter the list: ").split()))

    Ans = Divisible(value)
    print("Numbers divisible by both 3 and 5 are:", Ans)

if __name__ == "__main__":
    main()