# Zachary Murphy             9-25-25
# Lab #3 Section F - This Code Calculates distance and final velocity.

def distance(speed, time):
    return speed * time

def distanceCall():
    speed = int(input("Please Enter the Speed in Meters Per Second: "))
    time = int(input("Please Enter the time it took to travel in seconds: "))
    answer = distance(speed, time)
    print(f"The distance traveled is {answer} meters")

#----------------------------------------------------------------------

def final_velocity(initial_velocity, acceleration, time):
    return initial_velocity + (acceleration * time)

def final_velocityCall():
    initial_velocity = int(input("Please Enter the Initial Velocity in Meters Per Second :"))
    acceleration = int(input("Please Enter the Acceleration in Meters Per Second Per Second :"))
    time = int(input("Please Enter the Time in Seconds :"))
    answer = final_velocity(initial_velocity, acceleration, time)
    print(f"The Velocity of the object is now {answer} meters per second")