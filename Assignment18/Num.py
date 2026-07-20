#write a program which accept N number from user and store it into list.return addition of all prime number from  that list.main python file accept Nnumber from user and pass each number to chkprime() function which is part of our defined module named as MarvellousNum.Name of the function from main python file should be ListPrime()

def ChkPrime(No):
    if No<=1:
        return False
    for i in range(2,No):
        if No%i==0:
            return False
    return True




    
