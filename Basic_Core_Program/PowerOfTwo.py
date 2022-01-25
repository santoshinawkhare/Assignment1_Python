def find(n):
   if (n == 0): #if n value is assigned as 0
      return False
   while (n != 1): #if n value is not  as 1
      if (n % 2 != 0):
         return False
      n = n // 2
   return True
# find power of 2 is yes or no
if(find(4)):
   print('Yes')
else:
   print('No')




   #***********Algorithum*******
   #Input : n = 4
#Output : Yes
#2/2 = 4

#Input : n = 7
#Output : No

#Input : n = 32
##2/5 = 32