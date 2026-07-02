#write a lambda function which accept three numbers and returns largest number

Largest = lambda No1, No2, No3: No1 if No1 >= No2 and No1 >= No3 else (No2 if No2 >= No3 else No3)

def main():
    value1=int(input("enter the number:"))
    value2=int(input("enter the number:"))
    value3=int(input("enter the number:"))

    Ans=Largest(value1,value2,value3)
    print("Largest number is:",Ans)

if __name__=="__main__":
    main()