import pandas as pd
import random
from random import randint

s = input("How many sides on the dice?: ")

def rolldie(sides):
    value = randint(1,sides)
    return value

roll = rolldie(sides = int(s))

print(roll)