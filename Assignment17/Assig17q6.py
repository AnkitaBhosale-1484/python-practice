#write a program which accept one number  and disaply below pattern

def Pattern(No):
    for i in range(No,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

def main():
    value=int(input("enter the number"))
    Pattern(value)


if __name__=="__main__":
    main()