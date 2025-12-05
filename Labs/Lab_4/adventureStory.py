# Zachary Murphy             9-25-25
# Lab #4 Section F - This code will let the user play a choice based story.

print("Welcome! You are about to write your own story based on the choices you make. Your goal is to make it through the forest unscathed. Good Luck!")
print("Created By: Zach Murphy")
print("")

running = True
while running:
    direction = input(print("You're venturing down a path into the woods, and the path you're on diverges into three separate paths. Do you go [left], [straight], or [right]?"))
    if direction == "left":
        print("")
        log = input(print("You've chosen to go left. A little ways down this path, you find a fallen tree blocking your path. Do you try and [lift] the log out of your way, [jump] over the log and continue on your way, or [diverge] from the path and go around the log?"))
        if log == "lift":
            print("")
            print("You try to lift the log, but you skipped leg day, so you strain your leg and can't continue. The End.")
            running = False
        elif log == "jump":
            print("")
            print("You jump over the log, but roll you're ankle while landing. The End.")
            running = False
        elif log == "diverge":
            print("")
            bear = input(print("You walk around the log and continue down the path. Eventually, you come across a bear. It stairs you down, and looks as if it might attack you. Do you [run] back the way you came, [stand] your ground and yell at it, or take the fight to the bear and [charge] it?"))
            if bear == "run":
                print("")
                print("You run back the way you came, and leave the forest. The End.")
                running = False
            elif bear == "stand":
                print("")
                print("The bear starts to charge you, but turns and runs off before it gets to you. You continue down the path, and finally get out of the forest. The End, You Win.")
                running = False
            elif bear == "charge":
                print("")
                print("The bear mauls you and leaves you helpless in the forest. Obviously. The End.")
                running = False
            else:
                print("")
                print("Please Enter an Appropriate Answer. ")
        else:
            print("")
            print("Please Enter an Appropriate Answer. ")

#---------------------------------------------------------------------------   
    
    elif direction == "straight":
        print("")
        print("You decide to not switch directions, and you continue to walk. Eventually, you come to the end of the forest without any interruptions. The End, You Win. ")
        running = False

#----------------------------------------------------------------------------

    elif direction == "right":
        print("")
        water = input(print("You decide to turn down the path leading right. While walking, you come across a low point in the path that is covered in murky water. Do you [hope] the water isn't deep, and step into it, [jump] over the water, or [diverge] from the path and try to find a way around the water?"))
        if water == "hope":
            print("")
            print("You decide to trust that that the water isn't too deep, and step into. Luckily, the water is only a few inches deep, and your able to continue on your way. Eventually, you find your way out of the forest. The End, You Win.")
            running = False
        elif water == "jump":
            print("")
            print("You decide to jump over the standing water. Unfortunately, while planting your foot to jump, you slip and smack the back of your head on the ground, leaving you unconscious. The End.")
            running = False
        elif water == "diverge":
            print("")
            print("You decide to try to find a way around the standing water. While forging your own path around the water, you step in a ground hornet nest, and make them mad. They chase you all the way back to the beginning of the path your on. The End.")
            running = False
        else:
            print("")
            print("Please Enter an Appropriate Answer.")
    
#--------------------------------------------------------------------------

    else:
        print("")
        print("Please Enter an Appropriate Answer.")