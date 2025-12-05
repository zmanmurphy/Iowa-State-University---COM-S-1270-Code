# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code Calculates the velocity of an object/person using functions.

def final_velocity(initial_velocity, acceleration, time):
    # Definition = The rate of change of an object's position with respect to a frame of reference and time.
    # CITATION - https://byjus.com/physics/velocity/
    # CITATION - Date Accessed: 9-11-25

    return initial_velocity + (acceleration * time)

def main():
    initial_velocity = int(input("Please Enter the Initial Velocity in Meters Per Second :"))
    acceleration = int(input("Please Enter the Acceleration in Meters Per Second Per Second :"))
    time = int(input("Please Enter the Time in Seconds :"))
    answer = final_velocity(initial_velocity, acceleration, time)
    print(f"The Velocity of the object is now {answer} meters per second")

if __name__ == "__main__":
    main()