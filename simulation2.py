import pandas as pd
import random
from random import randint

x = input("How many simulations do you want to run?: ")

data = []                               # open list to collect data
for i in range(int(x)):
    black = random.randint(1,6)
    white = random.randint(1,6)
    combo = black * white
    d = {'black':black, 'white':white, 'combo':combo}  # dictionary of variables
    data.append(d)                      # appends the dictionary

df = pd.DataFrame(data)
print(df)

df.to_csv('simulation.csv')

totalsum = sum(item['combo'] for item in data)
print(totalsum)