#design python application that creates two seprate threads named even and odd
#even thred should display the first 10 even number
#the odd thread should display the first 10 odd number
#both threads should execute independently using the threading module
#ensure proper thread creation and execution

import time
import threading
def Even():
    print("first 10 even number")
    for i in range(2,21,2):
        print(i) 



def Odd():
    print("first 10 odd number:")
    for i in range(1,20,2):
        print(i)
    
def main():

    

    t1=threading.Thread(target=Even)
    t2=threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main thread")

    


if __name__=="__main__":
    main()