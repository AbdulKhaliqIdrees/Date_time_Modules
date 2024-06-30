#Learn How we Use time Module in Python Projects
from time import time,ctime,localtime
print("Use of time() Class")
a=time() #This Object return time in seconds
print(a)
print("Use of ctime() Class")
b=ctime() #This Object return Current Date and Time depend on PC
print(b)
c=ctime(a) #This Object Convert the seconds time into current date and time
print(c) 
print("Use of localtime() Class")
d=localtime() #This Object Return all attributes in the form of "tm_struct"
print(d)
print("Print With the Name of Attributes")
print("Year=",d.tm_year)
print("Month=",d.tm_mon)
print("Day=",d.tm_mday)
print("Hours=",d.tm_hour)
print("Minutes=",d.tm_min)
print("Seconds=",d.tm_sec)
print("With the Name of Index")
print("Year=",d[0])
print("Month=",d[1])
print("Day=",d[2])
print("Hours=",d[3])
print("Minutes=",d[4])
print("Seconds=",d[5])
