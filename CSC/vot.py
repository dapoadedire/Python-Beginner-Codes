"""
Write a program that accepts the age of someone and tells if the person is eligible to vote.
Make sure your program give'&s an error message if a user inputs an age less than 1 and greater than 119(oldest age alive).
Also, let the user know the amount of year it'll take for them to be eligible to vote.

Test Case:
Input: 15

Output: Oops. 
You're not eligible to vote. You will eligible in the next 3 years.

Test your code with the following ages: 257, - 5, 17, 19.
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

#Another angle

#Declare variable age
age = int(input("Input your age: "))

#First check if age is invalid.
if (age < 1) or (age > 119):
   print("Age is invalid")
#The only conditions that has not been checked are "Eligible" and "Not Eligible"
else:
   #The next line checks if the age is not eligible
   if (age < 18):
      print(f"You are not eligible to vote. \nYou will be eligible in the next {18- age} years.")
   #As usual, the else function does not check any condition, it is true as long as the preceeding if and elif are false.
   #The only condition that has not been checked is "Eligible"
   else:
      print("You are eligible to vote.")



print("I do hope you understand, if you don't, please send a dm.\Thanks")