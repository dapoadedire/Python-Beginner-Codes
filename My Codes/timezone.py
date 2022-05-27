import pytz
import datetime 
#for timezone in pytz.all_timezones:
 #  print (timezone)
 
#for c_timezone in pytz.common_timezones:
#   print(c_timezone)
   
xdate = datetime.datetime.now(pytz.timezone('Europe/London'))
x= xdate.strftime("%Y-%m-%d, %H:%M")

ydate = datetime.datetime.now(pytz.timezone('Africa/Lagos'))
y = ydate.strftime("%Y-%m-%d", %H:%M")

print(x)
print(y)


d_fro, m_fro, y_fro= map(int, y.split('-'))
d_to, m_to, y_to= map(int, x.split('-'))

fro = datetime.date(d_fro, m_fro, y_fro)
to = datetime.date(d_to, m_to, y_to)

diff =  to-fro
print(f"\nDifference is {diff.days*24} hours") 
 
	