# Zachary Murphy             9-11-25
# Lab #2 - This Code Calculates the current in amps of electricity.

# Definition = The flow of electron from one section of a circuit to another.
# CITATION - https://byjus.com/physics/current-electricity/
# CITATION - Date Accessed: 9-11-25

voltage = int(input("Please Enter the Voltage: "))
resistance = int(input("Please Enter the Resistance: "))

current = voltage/resistance

print(f"The current of electricity is {current} amps")