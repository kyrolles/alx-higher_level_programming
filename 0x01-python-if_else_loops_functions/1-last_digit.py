#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = str(number)
if int(x[-1]) == 0:
    print(f"Last digit of {number} is {x[-1]} and is 0")
elif int(x[-1]) > 5:
    print(f"Last digit of {number} is {x[-1]} and is greater than 5")
elif int(x[-1]) < 6:
    print(f"Last digit of {number} is {x[-1]} and is less than 6 and not 0")
    