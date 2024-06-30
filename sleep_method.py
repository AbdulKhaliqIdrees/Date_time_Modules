#Learn How we stop code during Run time with the help of sleep() method
from time import sleep
for i in range(20):
    print(i)
    if i==10:
        sleep(5)