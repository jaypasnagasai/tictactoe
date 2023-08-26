# Define a function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        # Join each cell in the row with '|' and print the row
        print(" | ".join(row))
        # Print a line of dashes to separate rows
        print("-" * 9)

# Define a function to check if a player has won
def check_winner(board, player):
    # Check each row for a complete line of the same player's symbol
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check each column for a complete line of the same player's symbol
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check both diagonals for a complete line of the same player's symbol
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Define a function to check if the board is full
def is_board_full(board):
    # Return False if any cell in the board is empty, otherwise return True
    return all(cell != " " for row in board for cell in row)

# Define the main game loop
def main():
    # Initialize an empty 3x3 Tic-Tac-Toe board
    board = [[" " for _ in range(3)] for _ in range(3)]
    # List of players' symbols: X and O
    players = ["X", "O"]
    # Variable to keep track of the current player's turn (0 for X, 1 for O)
    turn = 0

    # Start the game loop
    while True:
        # Determine the current player based on the turn
        current_player = players[turn % 2]
        # Print the current state of the board
        print_board(board)
        # Get the row and column input from the current player
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        # Check if the input is within valid range and the selected cell is empty
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            # Place the current player's symbol in the selected cell
            board[row][col] = current_player

            # Check if the current player has won
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            # Check if the board is full (a draw)
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            # Switch to the other player's turn
            turn += 1
        else:
            print("Invalid move. Try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
