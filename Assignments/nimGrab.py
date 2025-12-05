# Zachary Murphy             10-4-25
# Assignment #3
#
# This code will allow the user to play the game Nim with the computer or a person.

import random

print("NIMGRAB")
print("By: Zach Murphy")
print("[COM S 127 4]")

def main():
    running = True
    while running:
        choice1 = input(print("Would you like to [p]lay, [r]ead the rules, or [q]uit? "))
        if choice1 == "p":
            running2 = True
            while running2:
                choice2 = input(print("Would you like to play against a [c]omputer, a [p]erson, or [q]uit? "))
                
                if choice2 == "c":
                    running3 = True
                    removedNum = 0
                    computerNum = 0
                    while running3:
                        totalNum = 25 - removedNum
                        print(f"{totalNum} sticks remain.")
                        print("|" * totalNum)
                        personNum = int(input(print("Please Enter the number of sticks you would like to remove, 1, 2, or 3: ")))
                        if personNum < 1 or personNum > 3:
                            print("Please Enter an allowed number: ")
                        else:
                            totalNum = 25 - (removedNum + personNum)
                            if totalNum < 0:
                                print("Please Enter a number that won't make the number of sticks negative: ")
                            elif totalNum == 0:
                                print("Game Over, You Lost.")
                                running3 = False
                            else:
                                print(f"{totalNum} sticks remain.")
                                print("|" * totalNum)
                                if totalNum > 8:
                                    computerNum = random.randint(1, 3)
                                elif totalNum == 8:
                                    computerNum = 3
                                elif totalNum == 7:
                                    computerNum = 2
                                elif totalNum == 6:
                                    computerNum = 1
                                elif totalNum == 5:
                                    computerNum = random.randint(1, 3)
                                elif totalNum == 4:
                                    computerNum = 3
                                elif totalNum == 3:
                                    computerNum = 2
                                else:
                                    computerNum = 1
                                print(f"Computer removed {computerNum} sticks.")
                                removedNum = removedNum + computerNum + personNum
                                totalNum = 25 - removedNum
                                if totalNum == 0:
                                    print("Game Over, You Won!")
                                    running3 = False
                
                elif choice2 == "p":
                    running4 = True
                    player1Num = 0
                    player2Num = 0
                    playerTotalRemoved = player1Num + player2Num
                    while running4:
                        totalNum = 25 - playerTotalRemoved
                        print(f"{totalNum} sticks remain.")
                        print("|" * totalNum)
                        player1Num = int(input("Please Enter the number of sticks player 1 would like to remove, 1, 2, or 3: "))
                        if player1Num < 1 or player1Num > 3 :
                            print("Please Enter an allowed number: ")
                        else:
                            totalNum = 25 - (playerTotalRemoved + player1Num)
                            if totalNum < 0:
                                print("Please Enter a number that won't make the number of sticks negative: ")
                            elif totalNum == 0:
                                    print("Game Over, Player 2 Wins")
                                    running4 = False
                            else:
                                playerTotalRemoved = playerTotalRemoved + player1Num
                                running5 = True
                                while running5:
                                    totalNum = 25 - playerTotalRemoved
                                    print(f"{totalNum} sticks remain.")
                                    print("|" * totalNum)
                                    player2Num = int(input(print("Please Enter the number of sticks player 2 would like to remove, 1, 2, or 3: ")))
                                    if player2Num < 1 or player2Num > 3:
                                        print("Please Enter an allowed number: ")
                                    else:
                                        totalNum = 25 - (playerTotalRemoved + player2Num)
                                        if totalNum < 0:
                                            print("Please Enter a number that won't make the number of sticks negative: ")
                                        elif totalNum == 0:
                                            print("Game Over, Player 1 Wins")
                                            running4 = False
                                            running5 = False
                                        else:
                                            playerTotalRemoved = playerTotalRemoved + player2Num
                                            running5 = False
                
                elif choice2 == "q":
                    running2 = False

                else:
                    print("Please Enter an accepted letter: ")

        elif choice1 == "r":
            print("RULES")
            print("The goal of this game is to not be the person to take the last stick in the row of 25 sticks.")
            print("Each player will take 1, 2, or 3 sticks in turn until someone has taken the last stick.")
            print("Once the last stick has been taken, the game is over, and the person who took it loses the game.")

        elif choice1 == "q":
            print("Goodbye")
            running = False

        else:
            print("Please Enter and accepted letter: ")

if __name__ == "__main__":
    main()