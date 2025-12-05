# Zachary Murphy             9-25-25
# Lab #4 Section F - This Code uses other modules to calculate various values based on the user's need.

import myFinances
import myOhmsLaws
import myPhysics
import myShapes

def main():
    running = True
    while running:
        choice = input("Choice?: [F]inances, [O]hms, [P]hysics, [S]hapes, [Q]uit.")
        if choice == "F":
            choice2 = input("Finance Choice?: [A]PR, [C]ompound, [Q]uit.")
            if choice2 == "A":
                myFinances.aprCall()
            elif choice2 == "C":
                myFinances.accrued_amountCall()
            elif choice2 == "Q":
                print("Goodbye!")
                running = False
            else:
                print("ERROR: Please Enter an Appropiate Letter.")

        elif choice == "O":
            choice2 = input("Ohms Choice?: [R]esistance, [V]oltage, [C]urrent, [Q]uit.")
            if choice2 == "R":
                myOhmsLaws.resistanceCall()
            elif choice2 == "V":
                myOhmsLaws.voltageCall()
            elif choice2 == "C":
                myOhmsLaws.currentCall()
            elif choice2 == "Q":
                print("Goodbye!")
                running = False
            else:
                print("ERROR: Please Enter an Appropiate Letter.")
        
        elif choice == "P":
            choice2 = input("Physics Choice?: [D]istance, [V]elocity, [Q]uit.")
            if choice2 == "D":
                myPhysics.distanceCall()
            elif choice2 == "V":
                myPhysics.final_velocityCall()
            elif choice2 == "Q":
                print("Goodbye!")
                running = False
            else:
                print("ERROR: Please Enter an Appropiate Letter.")

        elif choice == "S":
            choice2 = input("Shapes Choice?: [C]ircle Area, [R]ectangle Area, [P]erimeter Rectangle, [Ci]rcumference, [Q]uit.")
            if choice2 == "C":
                myShapes.areaCircleCall()
            elif choice2 == "R":
                myShapes.areaCall()
            elif choice2 == "P":
                myShapes.perimeterCall()
            elif choice2 == "Ci":
                myShapes.circumferenceCall()
            elif choice2 == "Q":
                print("Goodbye!")
                running = False
            else:
                print("ERROR: Please Enter an Appropiate Letter.")

        elif choice == "Q":
            print("Goodbye!")
            running = False
        
        else:
            print("ERROR: Please Enter an Appropriate Letter.")

if __name__ == "__main__":
    main()