import math
def triangle(a, b, c):
     if (a==b==c):
       print("\nThe triangle is an equilateral triangle.\n") 
     elif (a==b) or (a==c) or (b==c):
       print("\nThe triangle is an isosceles triangle\n")
     else:
       print("\nThe triangle is a scalene triangle.\n")
#Using Heron's formula to find the area
     s = (a+b+c)/2
     area = math.sqrt(s*(s-a)*(s-b)*(s-c))
     area = "{:.2f}".format(area)
     print(f"\nThe area is {area}metres squared.\n")               
triangle(float(input("a : ")),
         float(input("b : ")), 
         float(input("c : "))
        ) 
         