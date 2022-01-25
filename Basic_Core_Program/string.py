##variable

flag = True
while(flag==True):
#Exception Try
    try:
        username = input("Enter your Name : ")
        if username.isalpha(): #condtion to check the entered input is alphabetic or not
            if len(username)>=3: #condition to check user name with atleast 3 chars
                print("Hello",username, "How are you ?")
                flag = False
            else:
                print ("User Name should atleast 3 charactor")
                flag = True
        else:
            print ("Invalid input please enter alphabates")
            flag = True

#Exception Catch
    except Exception as e:
        print(e)
        flag = True