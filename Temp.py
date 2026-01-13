Temperature = input("Enter Temperature in Celsius:")
Scale = input("Do you want it in Fahrenheit (Y) or Kelvin (N)?: ")
if(Scale == "Y"):
    ConvertF = int(Temperature) * 9 / 5 + 32
    print("Degrees in Fahrenheit: " + str(ConvertF))
if(Scale == "N"):
    ConvertK = int(Temperature) + 273.15
    print("Degrees in Kelvin: " + str(ConvertK))