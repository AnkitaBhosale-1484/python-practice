#write a program which contains one lambda function which accepts one parameter and return power of two

Power=lambda No:(2**No) 


def main():
    value=int(input("enter the number:"))
    Ans=Power(value)
    print("power of two:",Ans)

if __name__=="__main__":
    main()
