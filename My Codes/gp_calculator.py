"""
As an Engineer/Tech savy you are required to build a software engine in other words Compute a software programme to calculate and output students CGPA for a particular semester, where students will just input thier course codes and thier grades for each course up to the total number of core courses offered, and on this they just see thier total CGPA as an output from the Computing system.
🔥 🔥 🔥 ✌️😁
"""

import sys
import time


def slow_write(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
        
        
def total(tgp, tcu):
   cgpa ="{:.2f}".format(tgp/tcu)
   slow_write(f"\nYour CGPA is {cgpa}.")
   
def course():
   unit_list, gp_list = [], []
   n = int(input("How many core courses do you offer?"))
   for i in range(n):
     print(f"\nCourse {i+1}")
     #code = input("Course Code : ")
     unit, grade = int(input("Unit : ")), input("Grade : ").upper()
     
     if grade == "A":
       grade = 5
     elif grade == "B":
       grade = 4
     elif grade == "C":
       grade = 3
     elif grade == "D":
       grade = 2
     elif grade == "E":
       grade = 1
     elif grade == "F":
       grade = 0    
     gp = unit * int(grade) 
     
     gp_list.append(gp)
     unit_list.append(unit)
     
   tcu = sum(unit_list)
   tgp = sum(gp_list)
   total(tgp, tcu)
  
course()


   