import pandas as pd
import random
from random import randint

x = input("How many simulations do you want to run?: ")

data = []
for i in range(int(x)):
    colour = random.choice(["red","red","red","red","red","red","red","red","red", "black","black","black","black","black","black","black","black","black", "green"])
    if colour == "red":
        profit = 1
    else:
        profit = -1
    d = {"colour":colour, "profit":profit}
    data.append(d)

df = pd.DataFrame(data)
print(df)

df.to_csv('simulation.csv')

total_profit = sum(item['profit'] for item in data) # item is a variable name which allows for extraction of values

print("Your total profit is: " + str(total_profit))