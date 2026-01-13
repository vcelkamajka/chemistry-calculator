import random
from random import randint
import sys
import matplotlib.pyplot as plt
import numpy as np

choice = input("How many dice rolls would you like to roll?: ")

i = []
for diceroll in range(int(choice)):         # sets a new variable, 'diceroll' to play x times
    i.append(randint(1,6))            # adds to the empty list 'i' results from diceroll (1-6)
print(i)

x = [1,2,3,4,5,6]
y = [i.count(n) for n in range(1,7)]        # X,count function counts no. of n appearances. 1-7 covers 0-6

plt.bar(x, y)
plt.show()









next = input("Do you wish to proceed? Type Y for yes and N for no: ")
if next == "Y":
    ""
if next == "N":
    sys.exit()



for c in range(10):
    rank = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
    num = random.choice(["1", "2", "3"])
    print(f"{rank} {num}")       # f gives variables in string