import pandas as pd
import random
from random import randint
import matplotlib.pyplot as plt
import numpy as np


x = input("How many simulations do you want to run?: ")

data = []
for i in range(int(x)):
    colour = random.choice(['red','blue','green'])
    d = {'colour': colour}
    data.append(d)

df = pd.DataFrame(data)
print(df)

red = 0               # creats the variables and then sets them to 0
blue = 0
green = 0

for d in data:                      # loop to find each colour
    if d['colour'] == 'red':        # d['xyz'] goes into the list d and looks for red in the colour section
        red += 1
    if d['colour'] == 'blue':
        blue += 1
    if d['colour'] == 'green':
        green += 1

x = ['red', 'blue', 'green']
y = [red, blue, green]

min = min(red,blue,green)
print("The minimum value was: " + str(min))

max = max(red,blue,green)
print("The maximum value was: " + str(max))

print("The value for red was: " + str(red) + ", " + "The value for blue was: " + str(blue) + ", " + "The value for green was: " + str(green) + ".")

plt.bar(x, y)
plt.show()