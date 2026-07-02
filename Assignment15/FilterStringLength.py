# Write a lambda function using filter() which accepts a list of strings
# and returns a list of strings having length greater than 5.

Length = lambda Data: list(filter(lambda Str: len(Str) > 5, Data))

def main():
    value = input("Enter the strings: ").split()

    Ans = Length(value)
    print("Strings having length greater than 5:", Ans)

if __name__ == "__main__":
    main()