# Zachary Murphy             9-11-25
# Lab #2 - This Code Calculates the velocity of an object/person.

# Definition = The rate of change of an object's position with respect to a frame of reference and time.
# CITATION - https://byjus.com/physics/velocity/
# CITATION - Date Accessed: 9-11-25

initial_velocity = int(input("Please Enter the Initial Velocity in Meters Per Second :"))
acceleration = int(input("Please Enter the Acceleration in Meters Per Second Per Second :"))
time = int(input("Please Enter the Time in Seconds :"))

final_velocity = initial_velocity + (acceleration * time)
print(f"The Velocity of the object is now {final_velocity} meters per second")