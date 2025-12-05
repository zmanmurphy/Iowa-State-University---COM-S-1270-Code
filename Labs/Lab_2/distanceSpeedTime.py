# Zachary Murphy             9-11-25
# Lab #2 - This Code Calculates the distance traveled by an object/person.

# Definition = The amount of space between two places or things.
# CITATION - https://dictionary.cambridge.org/us/dictionary/english/distance
# CITATION - Date Accessed: 9-11-25

speed = int(input("Please Enter the Speed in Meters Per Second: "))
time = int(input("Please Enter the time it took to travel in seconds: "))

distance = speed * time
print(f"The distance traveled is {distance} meters")
