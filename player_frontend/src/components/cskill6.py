import random

# Define the board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check for win or draw
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    # Check for draw
    for row in board:
        if ' ' in row:
            return None  # Game is not over yet
    return 'Draw'

# AI makes a move with mistakes to let the player win
def ai_move(board):
    # 30% chance AI plays a random move (makes a mistake)
    if random.random() < 0.3:
        possible_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        if possible_moves:
            move = random.choice(possible_moves)
            board[move[0]][move[1]] = 'O'
            print("AI made a mistake!")
            return

    # Otherwise, AI plays optimally
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = 'O'

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Main game loop
def play_game():
    print("Tic-Tac-Toe: You are X, AI is O")
    print_board(board)
    while True:
        # Player move
        row, col = map(int, input("Enter your move (row and column 0, 1, or 2): ").split())
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'X'

        # Check for win or draw after player move
        result = check_winner(board)
        if result:
            print_board(board)
            if result == 'Draw':
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break

        # AI move
        ai_move(board)

        # Check for win or draw after AI move
        result = check_winner(board)
        if result:
            print_board(board)
            if result == 'Draw':
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break

        print_board(board)

# Start the game
if __name__ == "__main__":
    play_game()
    print("Vedant")