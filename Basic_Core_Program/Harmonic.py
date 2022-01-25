#variable
i = 1
harmonicValue = 0
flag = True

while(flag == True):
    #Exception Try block
    try :
        N = int(input("Enter the Nth harmonic number : "))

        if N > 0 :
            while (i<=N) :
                harmonicValue += 1/i
                i += 1
            print("Harmonic Value = ",harmonicValue)
            flag = False
        else :
            print("Enter the valid Nth value it cannot be 0 or less than that")
            flag = True

    #Exception catch Block
    except Exception as e :
        print(e)
        flag = True




#**************Harmonic number***************
        #H1 = 1 
       #H2 = H1 + 1/2 
#H3 = H2 + 1/3 
#H4 = H3 + 1/4 
#. 
#. 
#. 
#Hn = Hn-1 + 1/n 
 