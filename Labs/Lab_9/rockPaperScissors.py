# Zachary Murphy             11-6-25
# Lab #9 Section F

# This code will let the user play a best of 3, 5, or 7 rock paper scissors series against an AI.

def generateComputerMove():
    import random
    num = random.randint(1, 3)
    if num == 1:
        return "rock"
    elif num == 2:
        return "scissors"
    else:
        return "paper"
    
def playRound(playerMove):
    computerMove = generateComputerMove()
    print(f"Player's move is {playerMove}")
    print(f"Computer's move is {computerMove}")
    winner = determineWinner(playerMove, computerMove)
    if winner == playerMove:
        return "Player"
    elif winner == computerMove:
        return "Computer"
    else:
        return "Draw"

def determineWinner(playerMove, computerMove):
    if playerMove == "paper" and computerMove == "rock" or playerMove == "rock" and computerMove == "paper":
        return "paper"
    elif playerMove == "rock" and computerMove == "scissors" or playerMove == "scissors" and computerMove == "rock":
        return "rock"
    elif playerMove == "scissors" and computerMove == "paper" or playerMove == "paper" and computerMove == "scissors":
        return "scissors"
    else:
        return "draw"

def main():
    roundNum = int(input("Would you like to play a best of 3, 5, or 7? "))
    running = True
    playerTotal = 0
    computerTotal = 0
    while running:
        playerMove = str(input("Would you like to play paper, rock, or scissors? "))
        roundOutcome = playRound(playerMove)
        if roundOutcome == "Player":
            print("Player Wins the Round!")
            playerTotal += 1
            print(f"Player total wins: {playerTotal}")
        elif roundOutcome == "Computer":
            print("Computer Wins the Round!")
            computerTotal += 1
            print(f"Computer total wins: {computerTotal}")
        else:
            print("Draw!")
        if roundNum == 3 and playerTotal == 2:
            print("Player Wins the Series!")
            running = False
        elif roundNum == 3 and computerTotal == 2:
            print("Computer Wins the Series!")
            running = False
        elif roundNum == 5 and playerTotal == 3:
            print("Player Wins the Series!")
            running = False
        elif roundNum == 5 and computerTotal == 3:
            print("Computer Wins the Series!")
            running = False
        elif roundNum == 7 and playerTotal == 4:
            print("Player Wins the Series!")
            running = False
        elif roundNum == 5 and computerTotal == 4:
            print("Computer Wins the Series!")
            running = False


if __name__ == "__main__":
    main()