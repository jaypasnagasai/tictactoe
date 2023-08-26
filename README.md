# Tic-Tac-Toe Game

This is a simple Python implementation of the classic game Tic-Tac-Toe. The game is played in the console and supports two players.

## How to Play

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Open a terminal and run the following command to start the game:

```bash
python tic_tac_toe.py
```
1. Players will take turns entering their moves. The current state of the board will be displayed after each move.
2. Players should enter the row and column where they want to place their symbol (X or O), following the prompts.
3. The game will continue until one player wins or the board is full (a draw).

## Code Explanation

The `tic_tac_toe.py` file contains the Python code for the Tic-Tac-Toe game. Here's an overview of the main functions and their purposes:

`print_board(board)`: A function to print the Tic-Tac-Toe board with the current state.
`check_winner(board, player)`: A function to check if a player has won based on the current board state.
`is_board_full(board)`: A function to check if the board is completely filled, resulting in a draw.
`main()`: The main game loop where players take turns entering their moves and the game state is updated accordingly.

The game supports two players (X and O) and will display the winner or announce a draw when the game ends.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
