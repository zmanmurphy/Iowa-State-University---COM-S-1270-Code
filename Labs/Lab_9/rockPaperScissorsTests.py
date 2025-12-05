# Zachary Murphy             11-6-25
# Lab #9 Section F

# This code will test the functions within rockPaperScissors.py to make sure they work as intended.

from rockPaperScissors import generateComputerMove, determineWinner, playRound

def test_generateComputerMove():
    testMove = generateComputerMove()
    assert testMove == "paper" or testMove == "rock" or testMove == "scissors"

def test_determineWinner():
    assert determineWinner("rock", "paper") == "paper"
    assert determineWinner("scissors", "paper") == "scissors"
    assert determineWinner("paper", "paper") == "draw"

def test_playRound():
    testRound = playRound("paper")
    assert testRound == "Player" or testRound == "Computer" or testRound == "Draw"