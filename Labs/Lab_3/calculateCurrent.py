# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code Calculates the current in amps of electricity using functions.

def current (voltage, resistance):
    # Definition = The flow of electron from one section of a circuit to another.
    # CITATION - https://byjus.com/physics/current-electricity/
    # CITATION - Date Accessed: 9-11-25

    return voltage/resistance

def main():
    voltage = int(input("Please Enter the Voltage: "))
    resistance = int(input("Please Enter the Resistance: "))
    answer = current(voltage, resistance)
    print(f"The current of electricity is {answer} amps")

if __name__ == "__main__":
    main()