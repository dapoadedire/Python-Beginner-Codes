# Write a program that collects the values of the 3 sides of a triangle and tells the type of triangle(equilateral or) then proceeds to give the area and perimeter in 2 decimal places.

# Your program should be able to tell if a user inputs three values that are not the sides of a triangle, eg(23, 1, 3). 

# HINTS
# 💡 Use Heron's formula to calculate the area of a triangle. 

# 💡 The sum of the lengths of 2 sides of a triangle must be greater than—but not equal to—the length of the third side.


#We will need to import a module to peform some functions.
#The math module is used to peform functions such as square root, sin, round, etc
import math
#Declare variables for the three sides of the triangle

s1, s2, s3 = float(input("Value for side 1 : ")), float(input("Value for side 2 : ")), float(input("Value for side 3 : "))
#Check if the values given are that of a triangle. If the condition is not met, the else function that corresponds to this if function will take action.
if (s1 + s3 > s2) and (s2 + s1 > s3) and (s3 + s2 > s1):
    if s1 == s2 == s3:
        tri_type = "Equilateral"
    elif (s1 == s2) or (s2 == s3) or (s1 == s3):
        tri_type = "Isosceles"
    else:
        tri_type = "Scalene"
   
    s = (s1 + s2 + s3)/2
    #The math function is used in the next line
    area = math.sqrt(s * (s-s1) * (s-s2) * (s-s3))
    #The next line formats the area into 2 decimal places
    area = f"{area:.2f}" 
    print(f"\nThe area of the {tri_type} triangle({s1}, {s2}, {s3}) is {area}cm2 ")

#This runs when the first if condition is not met. 
else:
    print("\nYou are a mumu person. \nThis is not a triangle")


