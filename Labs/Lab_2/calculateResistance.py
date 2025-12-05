# Zachary Murphy             9-11-25
# Lab #2 - This Code Calculates the Resistance of an electrical current.

# Definition = The force that opposes electrical flow.
# CITATION - https://byjus.com/physics/electrical-resistance/
# CITATION - Date Accessed: 9-11-25

voltage = int(input("Please Enter the Voltage: "))
current = int(input("Please Enter the current in amps: "))

resistance = voltage/current

print(f"The resistance is {resistance} ohms")