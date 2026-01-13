import pandas as pd
import random
from random import randint

x = input("How many simulations do you want to run?: ")

data = []                               # open list to collect data
for i in range(int(x)):                 # runs x simulations
    roll = random.randint(1,6)    # roll variable runs x times getting values 1-6
    d = {"roll": roll}                  # adds roll to dictionary
    data.append(d)                      # appends (adds to list)

df = pd.DataFrame(data)                 # creats dataframe (excel spreadsheet esque)
print(df)

df.to_csv('simulation.csv')

