Python 2.7.4 (default, Apr  6 2013, 19:54:46) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

        
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(0,4):
    print turn + 1
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")
    if ship_row == guess_row and ship_col == guess_col:
        print "Congratulations! You sank my battleship!"
    elif guess_row < 4 or guess_col <4:
        print "Oops, that's not even in the ocean."
    elif board[int(guess_row)][int(guess_col)] == "X":
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[int(guess_row)][int(guess_col)] = "X"
        print_board(board)
        if turn == 3:
            print "Game Over"
            
print ship_row
print ship_col
