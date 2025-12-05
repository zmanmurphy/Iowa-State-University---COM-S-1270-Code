# Zachary Murphy             9-18-25
# Lab #3 Section F - This Code Calculates the distance traveled by an object/person using functions.

def distance(speed, time):
    # Definition = The amount of space between two places or things.
    # CITATION - https://dictionary.cambridge.org/us/dictionary/english/distance
    # CITATION - Date Accessed: 9-11-25

    return speed * time

def main():
    speed = int(input("Please Enter the Speed in Meters Per Second: "))
    time = int(input("Please Enter the time it took to travel in seconds: "))
    answer = distance(speed, time)
    print(f"The distance traveled is {answer} meters")

if __name__ == "__main__":
    main()
