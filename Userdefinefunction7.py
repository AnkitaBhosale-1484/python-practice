def Clculation(No1,No2):
        Mult=No1*No2
        Div=No1/No2
        return Mult,Div


def main():
        value1=int(input("enter first no:"))
        value2=int(input("enter secound no:"))

        Ret1,Ret2=Clculation(value1,value2)

        print("multiplication is:",Ret1)
        print("Division is:",Ret2)
      




if __name__=="__main__":
        main()