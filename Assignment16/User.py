#write a program which accept  number from user and print that number of "*" on screen 

def Show(No):
    for i in range(No):
        print("*",end="  ")

def main():
    value=int(input("enter the number"))
    Show(value)
    


if __name__=="__main__":
    main()