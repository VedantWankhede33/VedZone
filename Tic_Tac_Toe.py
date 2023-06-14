# Tic-Tac-Toe

# Initialize the board
board = [' ' for _ in range(9)]

# Define the winning combinations
winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

# Function to print the board
def print_board():
    print('-------------')
    for i in range(3):
        print('|', board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')
        print('-------------')

# Function to check if any player has won
def check_winner(player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'

    while True:
        print_board()
        print("It's player", current_player, "'s turn.")

        position = int(input('Enter the position (0-8): '))

        if board[position] == ' ':
            board[position] = current_player
            if check_winner(current_player):
                print_board()
                print('Congratulations! Player', current_player, 'wins!')
                break
            elif ' ' not in board:
                print_board()
                print("It's a tie!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('That position is already occupied. Try again.')

# Start the game
play_game()