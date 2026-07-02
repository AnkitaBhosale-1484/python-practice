#write a lambda function using fliter ()which accept a list  of numbers and return  a list of even number

Square=lambda Data:list(filter(lambda No:No % 2==0,Data))

def main():
    value=list(map(int,input("enter the list").split()))

    Ans=Square(value)
    print("list of even number is",Ans)

if __name__=="__main__":
    main()
    