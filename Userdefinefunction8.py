def BigBazar():
        print("inside Bigbazar")
        

        def Amul():
                print("inside amul icecream parlor")



def main():
        BigBazar() #allowed
        Amul() #error
        BigBazar.Amul() #error
       




if __name__=="__main__":
        main()