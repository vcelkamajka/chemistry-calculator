import sys
from dataclasses import asdict

avogadro = 6.022 * 10 ** 23

mw = input("What is the molecular mass of your compound (g/mol)?: ")
mass = input("What is the mass of your compound?: ")
try:
    mw = float(mw)
    mass = float(mass)
    print("Valid input")
except ValueError:
    print("Invalid input, retry with numbers.")
    sys.exit()

mass_unit = input("What is your mass unit of choice? kg = kg, g = g: ")
if mass_unit == 'kg':
    mass_2 = int(mass) * 1000
elif mass_unit == 'g':
    mass_2 = int(mass)
else:
    print("Please enter a mass unit in kg or g.")
    sys.exit()

mol = float(mass_2) / float(mw)
molecule_count = mol * avogadro
print("There are " + str(mol) + " moles and " + str(molecule_count) + " molecules.")

next_step = input("Would you like to calculate the concentration? (y/n): ")
if next_step == 'y':
    volume = input("What is the volume in L?: ")
if next_step == 'n':
    sys.exit()

conc_type = input("What concentration format? g/ml = g/ml, g/100ml = g/100ml Molarity = M, ppm = ppm: ")
if conc_type == 'g/ml':
    gml = float(mass) / float(float(volume) * 1000)
    print("The concentration is " + str(gml) + " g/ml")
if conc_type == 'g/100ml':
    g100ml = float(mass * 0.1) / float(volume)
    print("The concentration is " + str(g100ml) + " g/100ml")
if conc_type == 'M':
    molarity = float(mol) / float(volume)
    print("The molarity is " + str(molarity) + " M")
if conc_type == 'ppm':
    ppm = float(mass * 1000) / float(volume)
    print("The concentration is " + str(ppm) + " ppm")
else:
    print("Please enter a valid concentration format.")

