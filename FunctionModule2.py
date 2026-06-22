import Marvellous as MI  #alise karane mhanje topan name vapratat as ne

def main():
    print("enter first number:")
    value1=int(input())


    print("enter secound number:")
    value2=int(input())

    Ret=MI.Addition(value1,value2) 

    print("Addition is:",Ret)
    
if __name__ =="__main__":
    main()