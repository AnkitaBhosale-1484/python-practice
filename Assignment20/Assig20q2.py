#design a python application that creates two threads named EvenFactor  and Oddfactor 
#both threads should accept one integer number as a parameter 
#the evenFactor thread should:
#identity all even factors of the  given number
#calculate and display the sum of even factors
#the oddfactor thread should 
#identity all odd factor of the given number 
#calculate and display the sum of oddFactoe
#after both threads compleate execution the main thred should display the message "exit from main"

import threading
def Even(No):
    sum=0
    print(" even factor are")
    for i in range(1,No+1):
        if No%i==0:
            if i%2==0:
                print(i)
                sum=sum+i
    print("sum of even  factors:",sum)



def Odd(No):
    sum=0
    print(" odd factor are :")
    for i in range(1,No+1):
        if No%i==0:
            if i%2!=0:
             print(i)
             sum=sum+i

    print("sum of odd factors:",sum)
    
def main():

    value=int(input("eneter the number"))

    t1=threading.Thread(target=Even,args=(value,))
    t2=threading.Thread(target=Odd,args=(value,))


    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("End of main thread")

    


if __name__=="__main__":
    main()