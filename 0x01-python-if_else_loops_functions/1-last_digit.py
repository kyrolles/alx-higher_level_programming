#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# x = str(number)
# if int(x[-1]) == 0:
#     print(f"Last digit of {number} is {x[-1]} and is 0")
# elif int(x[-1]) > 5 and number > 0:
#     print(f"Last digit of {number} is {x[-1]} and is greater than 5")
# else:
#     print(f"Last digit of {number} is\
#  {x[-1] if number > 0 else (int(x[-1])*-1)}\
#  and is less than 6 and not 0")

x = str(number)

if number < 0:
    last_digit = int(x[-1]) * -1
else:
    last_digit = int(x[-1])

if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_digit}\
 and is less than 6 and not 0")
