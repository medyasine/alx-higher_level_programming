#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strnum = str(number)
if number < 0:
    r = "-" + strnum[-1]
else:
    r = strnum[-1]
if int(r) < 6 and int(r) != 0:
    print (f"Last digit of {number} is {r} and is less than 6 and not 0")
elif int(r) == 0:
    print (f"Last digit of {number} is {r} and is 0")
elif int(r) > 5:
    print (f"Last digit of {number} is {r} and is greater than 5")
