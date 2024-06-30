#Learn about strf() method
from datetime import datetime
a=datetime.today() #Give Current date
print(a)
b=a.strftime("%a-%b-%y")
print(b)
c=a.strftime("%A-%B-%Y")
print(c)
d=a.strftime("%d-%m-%y")
print(d)
e=a.strftime("%H::%M::%S")
print(e)
f=a.strftime("%I::%M::%S")
print(f)