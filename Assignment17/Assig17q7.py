#write a program which accept one number and display below pattern


def Display(No):
    for i in range(1,No):
        for j in range(1,No+1):
            print(j,end=" ")
        print()
        


def main():
    value=int(input("enter the number:"))
    Display(value)



if __name__=="__main__":
    main()