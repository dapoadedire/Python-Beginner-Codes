
import datetime 
print("Please, input the dates in the DD/MM/YYYY format.\n")
fro = input("\nDate from : ")
to = input("\nDate to : ")

try:
   fro = datetime.strptime(fro,"%d/%m/%Y").date()
   to  = datetime.strptime(to,"%d/%m/%Y").date()
   
   delta = to - fro
   print(f"\n{delta.days} days")		
   
except:
   print("\nError")
 
	