age = int(input("Input your age: "))
if (age < 1) or (age > 119):
   print("Age is invalid")
else:
   if (age < 18):
      print(f"You are not eligible to vote. \nYou will be eligible in the next {18- age} years.")
   else:
      print("You are eligible to vote.")
"""
#Declare variable "age"
age = int(input("Age: "))

#In this problem, there are there conditions to check--1) eligible to vote, 2) not eligible to vote, 3) Invalid age

#The if condition to check if age is Eligible  
if (18 >= age <=119):
    print("Eligible")
#The if condition to check if age is invalid.
elif (age < 18) and (age > 0):
    print(f"Not eligible, will be eligible in {18-age} years")
#The else function does not need a condition after it 'cos' it is true whenever previous if and elif conditions are false.
else:
    print("Age is invalid.")

"""

l = 0
while l < 11:
    if (l % 2) == 0:
        continue
    print(l)
    l += 1

    

#for i  in range(7):
 #   print(i)
