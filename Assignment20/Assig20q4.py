#design a python application that creates two threads named Thread1 and Thread2
#thread should display numbers from 1 to 50
#thread2 should display number from 50 to 1 reverse order 
#ensure that threads2 starts execution only after thread1 has completed
#use appropriate thread synchronization

import threading

def Thread1():
    for i in range(1,50+1):
        print(i)

def Thread2():
    for i in range(50,0,-1):
        print(i)

def main():

        T1=threading.Thread(target=Thread1)
        T2=threading.Thread(target=Thread2)

        T1.start()
        T1.join()
        
        T2.start()
        T1.join()
        

if __name__=="__main__":
    main()