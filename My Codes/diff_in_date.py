
import datetime 
print("\nPlease, input the dates in the YYYY-MM-DD format.")
date_from = input("\nDate from : ")
date_to = input("\nDate to : ")

try:
   y_from, m_from, d_from = map(int, date_from.     split('-'))
   y_to, m_to, d_to = map(int, date_to.split('-  '))

   f_date = datetime.date(y_from, m_from, d_from)
   l_date = datetime.date(y_to, m_to, d_to)

   f_date = datetime.date(y_from, m_from, d_from)
   l_date = datetime.date(y_to, m_to, d_to)

   delta = l_date - f_date
   print(f"\n{delta.days} days")		
   
except:
   print("\nError")
 
	