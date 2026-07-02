#write a lambda function which accept one number and returns cube of that number.


Cube=lambda No: No**3


def main():
    value=int(input("enter the number"))
    Ans=Cube(value)
    print("Cube of the number is",Ans)




if __name__=="__main__":
    main()

