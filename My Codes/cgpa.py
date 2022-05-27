        
def total(tgp, tcu):
   cgpa ="{:.2f}".format(tgp/tcu)
   print(f"\nYour CGPA is {cgpa}.")
   
def course():
   unit_list = []
   gp_list = []
   n = int(input("How many core courses do you offer?"))
   for i in range(n):
     print(f"\nCourse {i+1}")
     code = input("Course Code : ")
     unit = int(input("Unit : ")) 
     grade = input("Grade : ").upper()
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



   