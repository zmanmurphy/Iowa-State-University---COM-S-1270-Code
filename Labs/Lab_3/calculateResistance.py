# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code Calculates the Resistance of an electrical current using functions.

def resistance(voltage, current):
    # Definition = The force that opposes electrical flow.
    # CITATION - https://byjus.com/physics/electrical-resistance/
    # CITATION - Date Accessed: 9-11-25

    return voltage/current

def main():
    voltage = int(input("Please Enter the Voltage: "))
    current = int(input("Please Enter the current in amps: "))
    answer = resistance(voltage, current)
    print(f"The resistance is {answer} ohms")

if __name__ == "__main__":
    main()