# Zachary Murphy             9-25-25
# Lab #3 Section F - This Code Calculates current, voltage, and resistance.

def current (voltage, resistance):
    return voltage/resistance

def currentCall():
    voltage = int(input("Please Enter the Voltage: "))
    resistance = int(input("Please Enter the Resistance: "))
    answer = current(voltage, resistance)
    print(f"The current of electricity is {answer} amps")

#-------------------------------------------------------------------

def resistance(voltage, current):
    return voltage/current

def resistanceCall():
    voltage = int(input("Please Enter the Voltage: "))
    current = int(input("Please Enter the current in amps: "))
    answer = resistance(voltage, current)
    print(f"The resistance is {answer} ohms")

#----------------------------------------------------------------------

def voltage(current, resistance):
    return current * resistance

def voltageCall():
    current = int(input("Please Enter the Current: "))
    resistance = int(input("Please Enter the Resistance: "))
    answer = voltage(current, resistance)
    print(f"The Voltage is {answer}")