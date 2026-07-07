import Arithmetic 

def main():
    value1=int(input("enter the first number:"))
    value2=int(input("enter the secound number"))

    print("Addition is:",Arithmetic.Add(value1,value2))
    print("Substraction is:",Arithmetic.Sub(value1,value2))
    print("Division is:",Arithmetic.Div(value1,value2))
    print("Multiplication is",Arithmetic.Mult(value1,value2))


if __name__=="__main__":
    main()