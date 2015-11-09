# Hint:  use Google to find python function

from datetime import date, datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

a = datetime.strptime(date_start,"%m-%d-%Y")
b = datetime.strptime(date_stop,"%m-%d-%Y")

delta = b-a

print delta.days

####b)  
date_start = '12312013'  
date_stop = '05282015'

a = datetime.strptime(date_start,"%m%d%Y")
b = datetime.strptime(date_stop,"%m%d%Y")

delta = b-a

print delta.days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

a = datetime.strptime(date_start,"%d-%b-%Y")
b = datetime.strptime(date_stop,"%d-%b-%Y")

delta = b-a

print delta.days
