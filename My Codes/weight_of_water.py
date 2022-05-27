#python 3.7.1

def weight_calc():
     g = 9.81
     pi = 3.14159
     volume = float(pi) * float(radius) * float(radius) * float(height) 
     density = 997
     mass = volume * density
     weight = mass * g 
     mass = "{:.2f}".format(mass)
     weight ="{:.2f}".format(weight)
     print("The mass of the cylinder is\n" +str(mass) +" Kg") 
     print("")
     print("The weight of the cylinder is\n" +str(weight) +" N")
     


    
print("All units must be in metres!! ") 
print("")

should_continue = True

while should_continue == True:
   radius = input("\nWhat is the radius of the cylinder?\n")
  
   height = input("\nWhat is the height of the cylinder?\n")
    
   weight_calc()
   
   input("\nDo you want to run again? \n[Yes/No]\n")

   if run_again == "Yes":
       should_continue == True
    
   else:
       break
     
     
print("")    
print("Goodbye, thanks!")