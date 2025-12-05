# Zachary Murphy             12-1-25
# Assignment #6, Lecture Section 4, Lab Section F

# This code will allow up to four users to play Candy Realm, a take on the classic boardgame Candy Land.

import random

# yellow, green, blue, red, magenta, cyan

print("Candy Realm!")

print("By: Zachary Murphy")
print("[COM S 127 1]")

print("-----------------------------------------------------------------")
colorList = ["C", "Y", "B", "R", "M", "G"]
cardList = colorList

def checkWinner(player, playerScore):
    if playerScore == 58:
        print(f"Congratulations, player {player} wins!")
        return True
    else:
        return False

def moveDeck(deck):
    deck = deck[:7] + deck[10:]

    newCard = "  " + random.choice(cardList)

    deck = deck[:58] + newCard + deck[58:]
    return deck

def playerTurn(player, board, deck, playerScoreList):
    runningPlayer = True
    while runningPlayer:
        while True:
            try: # forces a correct input
                turnChoice = str(input(f"Player {player}, would you like to [d]raw, or [s]huffle?: "))
                if turnChoice == "d" or turnChoice == "s":
                    break
                else:
                    print("ERROR: Enter either [d] or [s]: ")
                    continue
            except TypeError:
                print("ERROR: Enter either [d] or [s]: ")
        
        if turnChoice == "d":
            card = deck[7]
            for space in range(playerScoreList[player-1]+1, 59):
                if card == board[space]:
                    playerScoreList[player-1] = playerScoreList[player-1] + (space - playerScoreList[player-1])
                    newdeck = moveDeck(deck)
                    return newdeck, playerScoreList
                elif space == 58:
                    print("There are no spaces ahead of you that match the top card on the deck.")
                    break
        elif turnChoice == "s":
            deck = createDeck()
            return deck, playerScoreList

def computerTurn(player, board, deck, playerScoreList):
    card = deck[7]
    for space in range(playerScoreList[player-1]+1, 59):
        if card == board[space]:
            spaceDiff = space - playerScoreList[player-1]
            if spaceDiff > 6 or spaceDiff + playerScoreList[player-1] == 58:
                playerScoreList[player-1] = playerScoreList[player-1] + spaceDiff
                deck = moveDeck(deck)
                return deck, playerScoreList
    
    deck = createDeck()
    return deck, playerScoreList

def createGraphic(board, deck): # creates the board that the user sees
    print("-----------------------------------------------------")
    print(" " * 7 + "1")
    print(" " * 7 + "2")
    print(" " * 7 + "3")
    print(" " * 7 + "4")
    print(board)
    print(deck)
    return [7, 7, 7, 7]

def updateGraphic(board, deck, playerScoreList): # updates the board after every action
    print("-----------------------------------------------------")
    print(" " * (playerScoreList[0]) + "1")
    print(" " * (playerScoreList[1]) + "2")
    print(" " * (playerScoreList[2]) + "3")
    print(" " * (playerScoreList[3]) + "4")
    print(board)
    print(deck)

def createDeck():
    deckList = []
    deck = "CARDS"
    for i in range(18): # creates a list of random cards using the six colors available
        newCard = random.choice(cardList)
        deckList.append(newCard)
    for i in range(len(deckList)): # turns list into string for graphic
        deck = deck + "  " + deckList[i]
    return deck

def createBoard():
    boardColorList = []
    board = "START"
    for i in range(18): # creates a list of colors at random using the six colors available
        newColor = random.choice(colorList)
        boardColorList.append(newColor)
    for i in range(len(boardColorList)): # turns the list into string used in the graphic
        board = board + "  " + boardColorList[i]
    board = board + "  " + "GOAL!"
    return board


def main():
    running = True
    while running:
        choice = input("MAIN MENU: [p]lay, [r]ules, or [q]uit?: ")
        
        if choice == "p":
            while True:
                try: # forces a correct input from the user
                    userCount = int(input("[1], [2], [3], or [4] human players?: "))
                        
                    if userCount < 1 or userCount > 4:
                        print(f"ERROR: {userCount} users isn't supported, please enter a valid number: ")
                        continue

                    break

                except ValueError:
                    print("ERROR: Enter a whole number please: ")

            
            board = createBoard()
            deck = createDeck()
            playerScoreList = createGraphic(board, deck)
            runningGame = True
            while runningGame:
                for player in range(1, userCount+1):
                    deck, playerScoreList = playerTurn(player, board, deck, playerScoreList)
                    updateGraphic(board, deck, playerScoreList)
                    if checkWinner(player, playerScoreList[player-1]):
                        while True:
                            try: # forces a correct input
                                playAgain = str(input("Would you like to play again? [y]es or [n]o: "))
                                if playAgain == "y":
                                    runningGame = False
                                    break
                                elif playAgain == "n":
                                    print("Goodbye!")
                                    running = False
                                    runningGame = False
                                    break
                                else:
                                    continue
                            except TypeError:
                                print("ERROR: Enter either [y] or [n]: ")
                        if playAgain == "n" or playAgain == "y":
                            break
                if runningGame == False:
                    break
                for computer in range(userCount+1, 5):
                    deck, playerScoreList = computerTurn(computer, board, deck, playerScoreList)
                    updateGraphic(board, deck, playerScoreList)
                    if checkWinner(computer, playerScoreList[computer-1]):
                        while True:
                            try: # forces a correct input
                                playAgain = str(input("Would you like to play again? [y]es or [n]o: "))
                                if playAgain == "y":
                                    runningGame = False
                                    break
                                elif playAgain == "n":
                                    print("Goodbye!")
                                    running = False
                                    runningGame = False
                                    break
                                else:
                                    continue
                            except TypeError:
                                print("ERROR: Enter either [y] or [n]: ")
                        if playAgain == "n" or playAgain == "y":
                            break
                
        
        elif choice == "r":
            print("On their turn, each player will decide to draw a card or shuffle the deck.")
            print("If a card is drawn, the player that drew the card will move to the next open space of the same color on the card.")
            print("If the player chooses to shuffle the deck, then the deck is shuffled and then it's the next player's turn.")
            print("The first player to reach the last space on the board wins.")
        
        elif choice == "q":
            print("Goodbye!")
            running = False
        
        else:
            print(f"ERROR: {choice} is not an option, please make a valid input: ")

if __name__ == "__main__":
    main()