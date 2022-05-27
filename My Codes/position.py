def position(number) :
   number= str(number)
   num_list= list(number)
   
   if num_list[-1]== "1":
     print(number + "st")


   elif num_list[-1]== "2":
     print(number + "nd")
 

   elif num_list[-1]== "3":
     print(number + "rd")
  
   else:
     print(number + "th")


#for i in range(int(input("How many times? "))):
position(input("Input a number"))
 
 