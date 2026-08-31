import sys
import pandas as pd
import numpy as np
from dataclasses import asdict
avogadro = 6.022 * 10 ** 23

    # start questions, necessary for calculator to work.

molecule_code = input("Please assign a code for the file: ")
molecule_name = input("What is the name of the molecule?: ")
molecular_weight = input("What is the molecular weight (g/mol)?: ")
x = int(input("How many decimal points would you like?: "))

print("----------Prepared Solution----------")

def moles_concentration(mass, molecular_weight, volume):
    moles = float(mass) / float(molecular_weight)
    molarity = float(moles) / float(volume)
    gml = float(mass) / float(float(volume) * 1000)
    g100ml = float(float(mass) * 0.1) / float(volume)
    ppm = float(float(mass) * 1000) / float(volume)
    molecules = float(mass) / float(molecular_weight) * avogadro
    return moles, molarity, gml, g100ml, ppm, molecules

intro_start = input("Do you have a solution made up? (y/n). For dilutions, input (n): ")
if intro_start == "y":
    mass = input("What is your mass? (g): ")
    volume = input("What is your volume? (L): ")

    # {} act as placeholders for values,
    # .format puts values into {}

    moles, molarity, gml, g100ml, ppm, molecules = moles_concentration(mass, molecular_weight, volume)
    print(f"You have {moles:.{x}f} moles;".format(moles, x))
    print(f"You have {molarity:.{x}f} moles/L;".format(molarity, x))
    print(f"You have {gml:.{x}f} g/mL;".format(gml, x))
    print(f"You have {g100ml:.{x}f} g/100mL;".format(g100ml, x))
    print(f"You have {ppm:.{x}f} ppm.".format(ppm, x))
    print(f"You have {molecules:e} molecules of {molecule_name}.".format(molecules,x))  # xyz:e makes it into scientific notation

    accumulated_for_prepared_data = []
    dp = {'Molecule Name': molecule_name, 'Molecular Weight (g/mol)': molecular_weight,
          'Mass (g)': mass, 'Moles (mol)': moles, 'Volume (L)': volume, 'Conc. (M)': molarity, 'Conc. (g/mL)': gml, 'Conc. (g/100mL)': g100ml, 'Conc. (ppm)': ppm}
    accumulated_for_prepared_data.append(dp)

    df_prepared = pd.DataFrame(accumulated_for_prepared_data)

    df_prepared.to_csv(f'Prepared {molecule_name}, {molecule_code}.csv')
    print(df_prepared)

if intro_start == "n":
    continue_0 = input("Would you like to continue to solution calculations? (y/n)? To access dilution calculations, input (d): ")
    if continue_0 == 'y':
        print("----------Solution Calculator----------")
    elif continue_0 == 'n':
        sys.exit()
    elif continue_0 == 'd':
        dilution = input("What are the units ? (M = moles/L, g = g/mL, g100 = g/100mL, p = ppm.: ")
        dilution_dictionary = {"M": "moles/L", "g": "g/mL", "g100": "g100ml", "p": "ppm"}
        unit = dilution_dictionary.get(dilution, dilution)
        c2 = input(f"What is the desired concentration? ({unit}): ")
        c1 = input(f"What is your current concentration? ({unit}): ")
        testc1c2 = float(c1) - float(c2)
        while testc1c2 < 0:
            print("Your starting concentration is too low!")
            try_again = input("Would you like to try again? (y/n): ")
            if try_again == 'y':
                c2 = input("What is the desired concentration? (Units as chosen prior): ")
                c1 = input("What is your current concentration? (Units as chosen prior): ")
            testc1c2 = float(c1) - float(c2)
            if testc1c2 > 0:
                break
            if try_again == 'n':
                print("Thank you for using this calculator!")
                sys.exit()
        v2 = input("What is your desired volume? (L): ")
        def dilution_function(c2, c1, v2):
            dilution_dictionary = {"M": "moles/L", "g": "g/mL", "g100": "g/100ml", "p": "ppm"}
            v1 = (float(c2) * float(v2)) / float(c1)
            unit = dilution_dictionary.get(dilution, dilution)
            dilution_response = f"You require {v1:.{x}f} L of {c1} {unit} {molecule_name} made up to {v2} L."
            return dilution_response

        accumulated_for_dilution_data = []
        v1 = (float(c2) * float(v2)) / float(c1)
        dd = {'Molecule Name': molecule_name, f'Initial Conc. ({unit})': c1, f'Final Conc. ({unit})': c2, 'Volume Required (L)': v1, 'Final Volume (L)': v2}
        accumulated_for_dilution_data.append(dd)

        dd_dilution = pd.DataFrame(accumulated_for_dilution_data)
        dd_dilution.to_csv(f'DC {molecule_name}, {molecule_code}.csv')
        print(dd_dilution)

        dilution_response = dilution_function(c2, c1, v2)
        dilution_selection = dilution_function(c2, c1, v2)
        print(dilution_selection)

        sys.exit()

    else:
        sys.exit()

def solution(mass, volume, moles, percent_solution, percent_solution_vol):
    percent_makeup = float(percent_solution) * float(percent_solution_vol)
    return percent_makeup, molar_solution

def choice():
    answer = input("Is a % solution required (y)? Select (n) for molarity: ")
    if answer == 'y':
        return "% solution"
    answer = input("Is a molar solution required (y/n): ")  # will retain in case of different solution set-up method needed.
    if answer == 'y':
        return "molar solution"
    else:
        print("Stopping calculator.")
        sys.exit()

selection = choice()
print("You chose:",selection)
if selection == "% solution":
    print("----------% Solution----------")
if selection == "molar solution":
    print("----------Molar Solution----------")

def percent_solution_function(percent_solution, percent_solution_vol):
    percent_makeup = float(percent_solution) * float(percent_solution_vol) * 10
    percent_solution_molarity = (float(percent_solution) * float(percent_solution_vol) * 10) / float(molecular_weight) / float(percent_solution_vol)
    return percent_makeup, percent_solution_molarity

if selection == '% solution':
    percent_solution = input("What % is required?: ")
    percent_solution_vol = input("What volume is required? (L): ")
    percent_makeup, percent_solution_molarity = percent_solution_function(percent_solution, percent_solution_vol)
    print(f"You need {percent_makeup:.{x}f} g of {molecule_name} in {percent_solution_vol} L. This is equivalent to {percent_solution_molarity:.{x}f} M.".format(percent_makeup, x))

    accumulated_for_solution = []
    ds = {'Molecule Name': molecule_name, '% Solution (g/100mL)': percent_solution,
          'Required Mass (g)': percent_makeup, 'Required Volume (L)': percent_solution_vol}
    accumulated_for_solution.append(ds)

    ds_solution = pd.DataFrame(accumulated_for_solution)

    ds_solution.to_csv(f'PS {molecule_name}, {molecule_code}.csv')
    print(ds_solution)

def molarity_solution_function(molarity_required, molecular_weight, molarity_volume):
    molarity_solution_mass = float(molarity_required) * float(molarity_volume) * float(molecular_weight)
    molarity_solution_percentage = (float(molarity_required) * float(molarity_volume) * float(molecular_weight) / 10) / float(molarity_volume)
    return molarity_solution_mass, molarity_solution_percentage

if selection == 'molar solution':
    molarity_required = input("What molarity is required?: ")
    molarity_volume = input("What volume is required? (L): ")
    molarity_solution_mass, molarity_solution_percentage = molarity_solution_function(molarity_required, molecular_weight, molarity_volume)
    print(f"You need {molarity_solution_mass:.{x}f} g of {molecule_name} in {molarity_volume} L. This is equivalent to a {molarity_solution_percentage}% solution.")

    accumulated_for_molarity = []
    dm = {'Molecule Name': molecule_name,'Required Molarity (M)': molarity_required, 'Required Mass (g)': molarity_solution_mass,'Required Volume (L)': molarity_volume}
    accumulated_for_molarity.append(dm)

    dm_molarity = pd.DataFrame(accumulated_for_molarity)

    dm_molarity.to_csv(f'MS {molecule_name}, {molecule_code}.csv')
    print(dm_molarity)
