def function(name = "Unknown"):
  print("My name is " + name)
  
function()
function("Farouq")

def func(x):
   return x**5
   
print(func(5)) 
print(func(3)) 
"""
def my_function(*kids):
  print("The youngest child is " + kids[-1])

my_function("Emil", "Tobias", "Linus")


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

"""