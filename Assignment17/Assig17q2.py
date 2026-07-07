#write a program which accept one number and display below pattern

def display(No):
    for i in range(No):
        for j in  range(No):
            print("*",end=" ")

        print()

def main():
    value=int(input("enter the number"))
    display(value)

if __name__=="__main__":
    main()