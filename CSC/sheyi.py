a = float(input("Enter first side: "))
b = float(input(" Enter second side: "))
c = float(input(" Enter third side: "))

Mode = int(input("one for Perimeter or two for Area: "))
s = (a+b+c)/2
if a+b<c or a+c<b or b+c<a:
    print("Wrong sides for a triangle")
elif Mode ==1:
       print("Perimeter is: ", a+b+c)
else:
       print("Area is: ",(s*(s-a)*(s-b)*(s-c))**0.5)



Mode = int(input("Enter 1 for Perimeter or 2 for Area: "))   
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
s = (a+b+c)/2
if a+b<c or a+c<b or b+c<a:
   print("This is not a triangle")
elif Mode ==1:
   print("Perimeter is: ", a+b+c)
else:
   print("Area is: ",(s*(s-a)*(s-b)*(s-c))**0.5)
     