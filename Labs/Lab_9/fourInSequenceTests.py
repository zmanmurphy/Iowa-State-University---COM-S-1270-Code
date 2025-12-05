# Zachary Murphy             11-6-25
# Lab #9 Section F

# This code will test multiple functions within the fourInSequence.py file to make sure they work as intended.

from fourInSequence import checkForNextMoveWin, checkAdjacent, checkDraw, checkWinner

def test_checkForNextMoveWin():
    testBoard = [[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "O", ".", ".", "."],
                [".", ".", ".", "O", ".", ".", "."],
                ["X", "X", "X", "O", ".", ".", "."]]
    assert checkForNextMoveWin(testBoard, 2) == 3
    testBoard2 = [[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "O", ".", ".", "."],
                ["X", "X", "X", "O", ".", ".", "."]]
    assert checkForNextMoveWin(testBoard2, 2) == -1

def test_checkAdjacent():
    testBoard = [[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "O", ".", ".", "."],
                ["X", "X", "X", "O", ".", ".", "."]]
    testNum = checkAdjacent(testBoard, 2)
    assert testNum == 2 or testNum == 3 or testNum == 4

def test_checkDraw():
    testBoard = [[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "O", ".", ".", "."],
                ["X", "X", "X", "O", ".", ".", "."]]
    assert checkDraw(testBoard) == False
    testBoard2 = [["X", "X", "X", "O", "X", "X", "X"],
                ["O", "O", "O", "X", "O", "X", "X"],
                ["X", "X", "X", "O", "O", "X", "X"],
                ["O", "O", "O", "X", "X", "O", "O"],
                ["X", "X", "X", "O", "O", "X", "X"],
                ["X", "X", "X", "O", "O", "X", "X"]]
    assert checkDraw(testBoard2) == True

def test_checkWinner():
    testBoard = [[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "O", ".", ".", "."],
                ["X", "X", "X", "O", ".", ".", "."]]
    assert checkWinner(testBoard, 2) == False
    testBoard2 = [[".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "O", ".", ".", "."],
                [".", ".", ".", "O", ".", ".", "."],
                [".", ".", ".", "O", ".", ".", "."],
                ["X", "X", "X", "O", "X", ".", "."]]
    assert checkWinner(testBoard2, 2) == True