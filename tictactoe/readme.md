# TicTacToe Project

This is a Python project that implements a command-line version of the Tic-tac-toe game. The game allows two players to take turns marking their signs ('x' and 'o') on a 3x3 board. The first player to get three of their signs in a horizontal, vertical, or diagonal line wins the game. If all the positions on the board are filled and no player has won, the game ends in a draw.

## Project Functions

1. `reset_board()`: This function initializes and returns a new empty game board as a list of strings.

2. `print_board(board)`: This function takes a game board as input and prints it to the console in a user-friendly format.

3. `gamestart()`: This function displays the game's introduction and initial empty board to the players.

4. `turn_player_1(board)`: This function handles the turn of player 1 ('x'). It prompts the player to choose a position on the board (1-9) and updates the board accordingly. It also checks if the chosen position is valid and handles any errors.

5. `winner_player_1(board)`: This function checks if player 1 has won the game by checking all the possible winning combinations on the board.

6. `turn_player_2(board)`: This function handles the turn of player 2 ('o'). It prompts the player to choose a position on the board (1-9) and updates the board accordingly. It also checks if the chosen position is valid and handles any errors.

7. `winner_player_2(board)`: This function checks if player 2 has won the game by checking all the possible winning combinations on the board.

8. `draw(board)`: This function checks if the game has ended in a draw by checking if all the positions on the board are filled.

9. `tictactoe()`: This function runs the main game loop. It initializes the board, displays the game start information, and alternates the turns between player 1 and player 2. It checks for a winner or a draw after each turn and ends the game accordingly.

## Usage

To play the Tic-tac-toe game, execute the following code at the command line:

**python tictactoe.py**

Follow the prompts on the console to choose the positions for your signs. The game will display the current board after each turn and announce the winner or a draw when the game ends.

Have fun playing Tic-tac-toe!
