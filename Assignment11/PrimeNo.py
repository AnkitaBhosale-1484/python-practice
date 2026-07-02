# Write a program which accepts one number and checks whether it is prime or not.

def CheackPrime(No):
    if No<=1:
        return False
    
    for i in range(2,No):
        if No % i==0:
            return False
    return True

def main():
    value=int(input("enter the number"))
    Ans=CheackPrime(value)
    
    if Ans==True:
        print("number is prime")
    else:
        print("number is not prime")

if __name__=="__main__":
    main()
    
