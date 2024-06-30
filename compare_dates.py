#Learn How we compare two dates
from datetime import date
a=date(2005,3,13)
b=date(2005,3,15)
c=date.today()
print(a>b) #This Give False 
print(c>a) #This Give True
#First he compare Years 
#If Years are same than he compare two months
#If Years and months are same than he compare dates