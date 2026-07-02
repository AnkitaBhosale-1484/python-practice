#Write a program which accepts one number and prints multiplication table of that number.


def multiplication_table(No):
    for i in range(1,11):
         print(No, "x", i, "=", No * i)
        


def main():
    value=int(input("enter the number"))
    multiplication_table(value)



if __name__=="__main__":
    main()
