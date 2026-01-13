import matplotlib.pyplot as plt
import numpy as np

Salary = input("Enter Salary: ")
Rent = input("Enter Yearly Rent: ")
Fixed_Expenditure = float(int(Salary) - int(Rent))
print(Fixed_Expenditure)

S = np.array([float(Salary)])
R = np.array([float(Rent)])

plt.plot(S, R)
plt.xlim(0, float(Salary)+100)
plt.plot(S, R)
plt.show
