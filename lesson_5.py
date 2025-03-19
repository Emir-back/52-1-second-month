# import random
#
# print(random.randint(2, 10))
from email.policy import default
from random import randint as random_number, choice

from termcolor import cprint
from decouple import config

import utilities.calculator as calc
from utilities.templates import Person

print(choice([1, 2, 5, 8, 0]))
print(random_number(10, 100))

print(calc.sub(10, 4))

p1 = Person('Bill', 20)
print(p1)

cprint("Hello, World!", "green", "on_red")

print(config('DATABASE_URL'))
commented = config('COMMENTED', default=0, cast=int)
print(commented * 2)