#Write a program which accepts one number and prints cube of that number.

def cube(No1):
    cub=No1**3
    return cub
def main():
    value=int(input("Enter the no"))
    Ans=cube(value)

    print("cube of number is:",Ans)

if __name__=="__main__":
    main()
    