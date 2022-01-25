def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("{0} is a leap year".format(Year))
  # Else it is not a leap year  
  else:  
    print("{0} is not a leap year".format(Year))
# Taking an input year from user  
Year = int(input("Enter the number: "))  
# Printing result  
CheckLeap(Year)  