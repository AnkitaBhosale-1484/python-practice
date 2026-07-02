#Write a program which accepts one number and prints square of that number.

def square(No1):
    sqr=No1*No1
    return sqr
def main():
    no=int(input("Enter the no:"))
    Ans=square(no)

    print("square of number is:",Ans)

if __name__=="__main__":
    main()

