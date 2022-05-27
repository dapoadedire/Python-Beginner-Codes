
import datetime 
print("\nPlease, input the dates in the YYYY-MM-DD format.")

date_from = input("\nDate from : ")
date_to = input("\nDate to : ")


d_fro, m_fro, y_fro= map(int, date_from.split('/'))
d_to, m_to, y_to= map(int, date_to.split('/'))

fro = datetime.date(d_fro, m_fro, y_fro)
to = datetime.date(d_to, m_to, y_to)

diff = fro - to
print(f"\n Difference is {diff.days} days") 
 
	