

# Number 2
f_name = input("First name : ")
s_name = input("Surname : ")

print("Hello,", s_name, f_name)

#umber 3

print("What do you call bla bla bla? \nA gummy bear ")

# 4
a = input("Input a number : ")
b = input("Input another number : ")
print(int(a) + int(b))


#5

a = int(input("A : ")) 
b = int(input("B : ")) 
c = int(input("C : ")) 

d = (a+b)/c

print(d)

#6

pizza_start = int(input("What number of slices did you start with? : "))
pizza_left = int(input("What number of slices do you have left? : ")) 

diff = pizza_start - pizza_left

print(f"You have {diff} slices of pizza left ")
print("You have", diff, "slices of pizza left")

#7

name = input("Name : ")
age = int(input("Age : ")) 

print(f"{name} next birthday, you will be {age + 1}")

#8



price = int(input("Total price(USD) : ")) 
dinner = int(input("Number of dinners(USD) : "))
ppd = price/dinner
print(f"Each dinner pays {ppd} USD")

"""

#9
days = int(input("Input the number of days : "))
hours = 24*days
minutes = 60*hours
seconds = 60*minutes

print(f"{hours} hours")
print(f"{minutes} minutes")
print(f"{seconds} seconds")
#10

"""
weight_kg = int(input("Input weight in kilograms : ")) 

weight_pounds = weight_kg*2204
print(f"{weight_kg} kilograms is equal to {weight_pounds} pounds")

#11


over100 = int(input("Input a number over 100 : "))
under10 = int(input("Input a number under 10 : "))
divide = over100 % under10

print(f"{over100} can be divided by {under10} {divide}times without remainder")
