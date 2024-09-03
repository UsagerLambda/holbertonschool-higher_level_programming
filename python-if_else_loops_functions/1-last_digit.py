#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10  # last_digit prend le dernier chiffre de number
if number < 0:  # si number est négatif
    if number % 10 > 0:
        last_digit -= 10  # ont soustrait 10 au dernier
        # nombre pour avoir la valeur correct

if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
else:
    print(
        f"Last digit of {number} is {last_digit} "
        "and is less than 6 and not 0"
        )
