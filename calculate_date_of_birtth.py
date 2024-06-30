#Learn How we Calculate date of Birth
from datetime import date
birth=date(year=2003,month=2,day=15) #Date of Birth
tday=date.today() #Current date and Time
print(tday)
age=tday.year-birth.year-((tday.month,tday.day)<(birth.month,birth.day))
print(age) #Total age
