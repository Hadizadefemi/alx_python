#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = number

if number < 0:
    number = -1 * number

last_digit = number % 10

if new_number < 0:
    last_digit = -1 * last_digit

output = f"Last digit of {new_number} is {last_digit} and is "
if last_digit > 5:
    output += "greater than 5"
elif last_digit == 0:
    output += "0"
elif (last_digit < 6) and (last_digit != 0):
    output += "less than 6 and not 0"

print(output)
