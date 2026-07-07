#write a program which accept number from user and return number of digits in that number 

def digit(No):
    count=0
    while(No>0):
        count=count+1
        No=No//10
    return count



def main():
    value=int(input("enter number:"))
    Ans=digit(value)
    print("number of digits:",Ans)



if __name__=="__main__":
    main()