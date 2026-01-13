import random
from random import randint
import sys
from numpy.ma.core import where

i = input("Pick an integer between 1 and 10: ")
try:                                                                        # condition set up
    int(i)
    if not 1 <= int(i) <= 10:
        raise ValueError                                                    # Error set-up
    print("Valid input")
except ValueError:                                                          # Prints error rather than proceeding/giving nothing
    print("Invalid input, retry with an integer between 1 and 10.")
    sys.exit()                                                              # Ends run

random_number = randint(1, 10) # Integer random number

if random_number == int(i):
    print("Correct!")
elif random_number != int(i):
    print("Incorrect!")
    print("Correct number was: " + str(random_number))

diff = abs(random_number - int(i))
if diff != 0:
    print("You were off by " + str(diff) + ", better luck next time.")
elif diff == 0:
    ""


