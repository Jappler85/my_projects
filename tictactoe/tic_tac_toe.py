# TicTacToe

# 1. Function for resetting the board 
def reset_board():
    board = [" " for x in range(9)]
    return board


# 2. Function to print the board
def print_board(board):
    toprow = " ___ ___ ___"
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    bottomrow = (" ‾‾‾ ‾‾‾ ‾‾‾") 
    print(toprow)
    print(row1)
    print(row2)
    print(row3)
    print(bottomrow)


# 3. Function for startup & import clear_output 
from IPython.display import clear_output
def gamestart():
    print("Welcome to Tic Tac Toe!")
    print()
    print("This is your board:")
    print(" ___ ___ ___")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(" ‾‾‾ ‾‾‾ ‾‾‾") 
    print("At the beginning it will be empty.")
    print("Each turn, fill in a Number from 1-9 to mark your sign.")
    print("Player 1 is 'x', Player 2 is 'o'")


# 4. Turn player 1
def turn_player_1(board):
    x = int(input("Player 1 (x), please make your sign (1-9)"))
    clear_output()
    if board[x - 1] == " ":
        board[x - 1] = "x" 
        print(str(x) + " - excellent choice, player 1!")
        print()
        print("This is the current Board:")
        print_board(board)
        print("It's your turn, player 2")
    else:
        print("This place is already taken!")
        print("Please try again, player 1")
        print("This is the current Board:")
        print_board(board)
        print()
        turn_player_1(board)


# 4.a. Check winning condition for player 1
def winner_player_1(board):
    if (board[0] == "x" and board[1] == "x" and board[2] == "x") or \
       (board[3] == "x" and board[4] == "x" and board[5] == "x") or \
       (board[6] == "x" and board[7] == "x" and board[8] == "x") or \
       (board[0] == "x" and board[3] == "x" and board[6] == "x") or \
       (board[1] == "x" and board[4] == "x" and board[7] == "x") or \
       (board[2] == "x" and board[5] == "x" and board[8] == "x") or \
       (board[0] == "x" and board[4] == "x" and board[8] == "x") or \
       (board[2] == "x" and board[4] == "x" and board[6] == "x"):
        return True
    else:
        return False


# 5. Turn player 2
def turn_player_2(board):
    x = int(input("Player 2 (0), please make your sign (1-9)"))
    clear_output()
    if board[x - 1] == " ":
        board[x - 1] = "o" 
        print(str(x) + " - excellent choice, player 2!")
        print()
        print("This is the current Board:")
        print_board(board)
        print("It's your turn, player 1")
    else:
        print("This place is already taken!")
        print("Please try again, player 2")
        print("This is the current Board:")
        print_board(board)
        print()
        turn_player_2(board)


# 5.a. Check winning condition for player 2
def winner_player_2(board):
    if (board[0] == "o" and board[1] == "o" and board[2] == "o") or \
       (board[3] == "o" and board[4] == "o" and board[5] == "o") or \
       (board[6] == "o" and board[7] == "o" and board[8] == "o") or \
       (board[0] == "o" and board[3] == "o" and board[6] == "o") or \
       (board[1] == "o" and board[4] == "o" and board[7] == "o") or \
       (board[2] == "o" and board[5] == "o" and board[8] == "o") or \
       (board[0] == "o" and board[4] == "o" and board[8] == "o") or \
       (board[2] == "o" and board[4] == "o" and board[6] == "o"):
        return True
    else:
        return False


# 6. Check for draw
def draw(board):
    if " " not in board:
        return True
    else:
        return False

# 7. Running the program (insert Functions 1-6)
def tictactoe():
    x = reset_board()
    clear_output()
    gamestart()
    print_board(x)
    while True:
        turn_player_1(x)
        if winner_player_1(x) is True:
            print()
            print("Player 1 wins!")
            break
        elif draw(x) is True:
            print()
            print("It's a draw!")
            break
        turn_player_2(x)
        if winner_player_2(x) is True:
            print()
            print("Player 2 wins!")
            break
        elif draw(x) is True:
            print()
            print("It's a draw!")
            break



# Tic-tac-toe game
if __name__ == "__main__":
    tictactoe()
    # Start a new round of Tic-tac-toe
