from datetime import datetime 
from datetime import timedelta 

#begin = input("Beginning Day (in DD/MM/YYYY) : ")
x = int(input("How many days do you want to add? \n")) 
#begin = datetime.strptime(begin,"%d/%m/%Y").date()
begin = datetime.now() 
begins = begin.strftime("%b %d %Y")

print(f"Beginning date : {begins}") 


end = begin + timedelta(days=x)
ends = end.strftime("%b %d %Y")

print(f"Ending date : {ends}")



