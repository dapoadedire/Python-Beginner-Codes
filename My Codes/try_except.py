"""
try:
   print(7/0)
except ZeroDivisionError:
   print("Zero Division Error")
except (ValueError, TypeError) :
   print("Type Error")
finally:
   print("This code will run no matter what")
  """
 
try:
   print(1/0)
except ZeroDivisionError:
   print(1/0)
else:
   print(6)