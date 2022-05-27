age = int(input("Enter the age: "))
a = 18 - age

if age < 0 or age > 119:
    print("Age is not valid, please try again.")
elif age > 0 and age < 18:
    print("Oops, you are not eligible to vote. \nYou will be eligible to vote in the next,", a ,"years.")
    print(f"Oops, you are not eligible to vote. \nYou will be eligible to vote in the next {a} years.") #best way to format strings
    print("Oops, you are not eligible to vote. \nYou will be eligible to vote in the next %d years."%(a))
elif age >= 18 and age <= 119:
    print("Yayyyy, you are eligible to vote")