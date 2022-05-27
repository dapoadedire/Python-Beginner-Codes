a = float(input("Enter the first length\na: "))
b = float(input("Enter the second length\nb: "))
c = float(input("Enter  third length\nc: "))

	
if (a+b)> c and (a+c)>b and (b+c)>a:
    d = (a+b+c)/2
    s = round (d,2)
    Area = (s*(s-a)*(s-b)*(s-c))**0.5
    if a == b == c:
        print ("\nEquilateral triangle")
    elif a!=b!=c:
        print("\nScalene triangle")
    elif a == b or a ==c or b == c:
        print("\nIsosceles triangle")

    print ("Area:", round (Area,2))
else:
   	print("The three values are not sides of a triangle")