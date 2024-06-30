#Learn How we Use datetime Module in Python Projects
from datetime import datetime,date,time,timedelta
print("Use of datetime() Class")
a=datetime(year=2021,month=2,day=15) #This Object Return the Given Date and time Year,Month,Day are Compulsary
print(a)
b=datetime(year=2022,month=5,day=15,hour=18,minute=45,second=55)
print(b)
c=datetime(2023,12,23,20,33,59) #This Format also used for date and time
print("Year=",a.year) #We Can also print a single attribute with the name of "object.attribute_name"
print("Month=",b.month) #We Can also print a single attribute with the name of "object.attribute_name"
print("Second=",c.second) #We Can also print a single attribute with the name of "object.attribute_name"
e=datetime.today() #This Object return Current date and time
print(e)
f=datetime.now()  #This Object return Current date and time
print(f)
print("Day=",e.day) #We Can also print a single attribute with the name of "object.attribute_name"
print("Hour=",e.hour) #We Can also print a single attribute with the name of "object.attribute_name"
print("Second=",f.second) #We Can also print a single attribute with the name of "object.attribute_name"
print("Use of date() class")
g=date(day=15,month=2,year=2003) #This Object return us only Given Date
print(g)
print("Year=",g.year) #We Can also print a single attribute with the name of "object.attribute_name"
print("Month=",g.month) #We Can also print a single attribute with the name of "object.attribute_name"
print("Day=",g.day) #We Can also print a single attribute with the name of "object.attribute_name"
h=date.today() #This Object Give us only Current date
print(h)
print("Year=",h.year) #We Can also print a single attribute with the name of "object.attribute_name"
print("Month=",h.month) #We Can also print a single attribute with the name of "object.attribute_name"
print("Day=",h.day) #We Can also print a single attribute with the name of "object.attribute_name"
i=time(second=15,minute=2,hour=23) #This Object return us only Given time
print(i)
print("Hour=",i.hour) #We Can also print a single attribute with the name of "object.attribute_name"
print("Minute=",i.minute) #We Can also print a single attribute with the name of "object.attribute_name"
print("Second=",i.second) #We Can also print a single attribute with the name of "object.attribute_name"
print("Use of timedelta() class")
#Object of timedelta() class is used to find Duration between two dates,difference between two dates
#Object of timedelta() class is used to find future dates of previous dates
x=timedelta(days=6)
y=date.today() #This object give us current date
print(y)
z=y+x  #This Object give us Future Date according to days of timedelta object
print(z)
l=y-x #This Object give us previous Date according to days of timedelta object
print(l)