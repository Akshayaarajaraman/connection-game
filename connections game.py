def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    # Check horizontal
    for row in board:
        for i in range(len(row) - 3):
            if all(cell == player for cell in row[i:i+4]):
                return True

    # Check vertical
    for col in range(len(board[0])):
        for i in range(len(board) - 3):
            if all(board[row+i][col] == player for row in range(4)):
                return True

    # Check diagonal (from top-left to bottom-right)
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            if all(board[i+k][j+k] == player for k in range(4)):
                return True

    # Check diagonal (from top-right to bottom-left)
    for i in range(len(board) - 3):
        for j in range(3, len(board[0])):
            if all(board[i+k][j-k] == player for k in range(4)):
                return True

    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def connect_four():
    rows = 6
    cols = 7
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        column = int(input(f"Player {player}, choose a column (1-{cols}): ")) - 1

        # Check if the chosen column is valid
        if 0 <= column < cols and board[0][column] == ' ':
            # Find the first available row in the chosen column
            for row in range(rows - 1, -1, -1):
                if board[row][column] == ' ':
                    board[row][column] = player
                    break

            # Check for a winner or a tie
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch to the next player's turn
            turn += 1
        else:
            print("Invalid move. Please choose a valid column.")


