"""
Day 17.
📍Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

🤗🤸‍♀️
"""


for num in range(0,3000):     
     if ("2" in str(num)) and ("4" in str(num)) and ("6" in str(num)) and ("8" in str(num)) :
          print(num, end=" ")         
               
         
   