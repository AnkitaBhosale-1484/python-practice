#write a program which accept one number for user and cheack weather  number is prime or not 

def ChkPrime(No):
    if No<=1:
        return False
    
    for i in range(2,No):
        if No%i==0:
            return False
    return True


def main():
   value=int(input("enter the number"))
   Ans=ChkPrime(value)


   if Ans==True:
       print("number is prime")
   else:
       print("number is not prime")



if __name__=="__main__":
    main()