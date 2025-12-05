# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code Calculates the voltage of an electric current using functions.

def voltage(current, resistance):
    # Definition = The pressure from an electrical circuit's power source that pushes charged electrons (current) through a conducting loop.
    # CITATION - https://www.fluke.com/en-us/learn/blog/electrical/what-is-voltage?srsltid=AfmBOoo_KqTZ06T7vsQqc8zM_uN5LgtX71_dw9JrTPSjew0Nr629DxFL
    # CITATION - Date Accessed: 9-11-25

    return current * resistance

def main():
    current = int(input("Please Enter the Current: "))
    resistance = int(input("Please Enter the Resistance: "))
    answer = voltage(current, resistance)
    print(f"The Voltage is {answer}")

if __name__ == "__main__":
    main()