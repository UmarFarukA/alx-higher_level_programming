#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number != 0 and number < 6:
    s = (f'Last digit of {number} is '
         f'{last_digit} and is less than 6 and not 0')
    print(s)
elif last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
