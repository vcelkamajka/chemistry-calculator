temperature = input("Enter temperature in Celsius: ")

def temp_convert(temperature):
    convertF = float(temperature) * 9 / 5 + 32
    convertK = float(temperature) + 273.15
    return convertF, convertK

F, K = temp_convert(temperature)    # the F, K acts as variable for convertF and convertK - any thing can be used here.

print(f"Fahrenheit: {F:.2f}°F")
print(f"Kelvin: {K:.2f} K")
