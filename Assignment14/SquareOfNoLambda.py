#write a lambda function which accept one number and returns square of that number.

Square=lambda No:No*No

def main():

    value=int(input("enter the number"))
    Ans=Square(value)
    print("square of the number is",Ans)



if __name__=="__main__":
    main()


