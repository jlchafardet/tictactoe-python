import os
import sys
import json

# ANSI color codes for colored text in the console
colors = {
    'reset': "\x1b[0m",   # Resets text color to default
    'blue': "\x1b[34m",   # Sets text color to blue (Player)
    'red': "\x1b[31m",    # Sets text color to red (Computer)
    'yellow': "\x1b[33m", # Sets text color to yellow (Grid)
    'green': "\x1b[32m",  # Sets text color to green
}

# Game board initialized as a 3x3 grid filled with spaces
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Variables to keep track of results
player_wins = 0
computer_wins = 0
ties = 0

# Variable to keep track of whose turn it is; starts with 'Player'
current_player = 'Player'

# Path to the records file
records_file = 'tictactoe_records.json'

# Variable to determine if the computer should play smart
smart_opponent = False

def load_records():
    """
    Load game records from a JSON file.
    If the file doesn't exist or is corrupted, initialize records to zero.
    """
    global player_wins, computer_wins, ties
    if os.path.exists(records_file):
        try:
            with open(records_file, 'r') as file:
                data = json.load(file)
                player_wins = data.get('player_wins', 0)
                computer_wins = data.get('computer_wins', 0)
                ties = data.get('ties', 0)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading records file: {e}")
            player_wins = computer_wins = ties = 0
    else:
        # If the file doesn't exist, initialize records
        player_wins = computer_wins = ties = 0
        save_records()

def save_records():
    """
    Save game records to a JSON file.
    """
    data = {
        'player_wins': player_wins,
        'computer_wins': computer_wins,
        'ties': ties
    }
    try:
        with open(records_file, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving records: {e}")

def clear_screen():
    """
    Clear the console screen for better readability.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def render_board():
    """
    Render the game board with colors and position numbers.
    """
    clear_screen()  # First, clear the screen
    print(f"{colors['yellow']} Tic Tac Toe {colors['reset']}")  # Display the game title in yellow
    print()  # Add an empty line for spacing

    position = 1  # Start position numbering from 1

    # Loop through each row of the board
    for i in range(3):
        row = ''  # Initialize an empty string to build the row display
        # Loop through each column in the current row
        for j in range(3):
            cell = board[i][j]  # Get the value of the current cell
            if cell == 'X':
                # If the cell has an 'X', display it in blue (Player)
                row += f"{colors['blue']} X {colors['reset']}"
            elif cell == 'O':
                # If the cell has an 'O', display it in red (Computer)
                row += f"{colors['red']} O {colors['reset']}"
            else:
                # If the cell is empty, display the position number
                row += f" {position} "
            if j < 2:
                row += '|'  # Add a vertical separator between cells, but not after the last one
            position += 1
        print(row)  # Print the constructed row
        if i < 2:
            print(f"{colors['yellow']}---+---+---{colors['reset']}")  # Add horizontal separators between rows, colored yellow
    print()  # Add another empty line for spacing

def check_winner():
    """
    Check if there's a winner or if the game is a tie.
    Returns 'X' if the player wins, 'O' if the computer wins, 'Tie' if it's a tie, or None if the game is still ongoing.
    """
    # Define all possible winning combinations: rows, columns, and diagonals
    lines = [
        # Rows
        [ [0,0], [0,1], [0,2] ],
        [ [1,0], [1,1], [1,2] ],
        [ [2,0], [2,1], [2,2] ],
        # Columns
        [ [0,0], [1,0], [2,0] ],
        [ [0,1], [1,1], [2,1] ],
        [ [0,2], [1,2], [2,2] ],
        # Diagonals
        [ [0,0], [1,1], [2,2] ],
        [ [0,2], [1,1], [2,0] ]
    ]

    # Iterate through each possible winning line
    for line in lines:
        a, b, c = line  # Destructure the three positions in the line
        if (board[a[0]][a[1]] != ' ' and
            board[a[0]][a[1]] == board[b[0]][b[1]] and
            board[a[0]][a[1]] == board[c[0]][c[1]]):
            return board[a[0]][a[1]]  # If all three cells match, return the winner ('X' or 'O')

    # Check if the board is full without any winner, resulting in a tie
    for row in board:
        if ' ' in row:  # If any cell is still empty
            return None  # The game is still ongoing

    return 'Tie'  # If no empty cells and no winner, it's a tie

def get_player_move():
    """
    Prompt the player to make a move.
    """
    while True:
        try:
            answer = input('Enter your move (1-9): ').strip()
            position = int(answer)
            if 1 <= position <= 9 and is_valid_move(position):
                row, col = divmod(position-1, 3)
                board[row][col] = 'X'  # Place an 'X' on the board at the specified position
                break  # Exit the loop after a valid move
            else:
                print("Invalid move. Try again.")  # Inform the player of an invalid move
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")  # Handle non-integer input
    next_turn()  # Proceed to the next turn

def get_computer_move():
    """
    Determine the computer's move.
    """
    if smart_opponent:
        best_move = minimax(board, 'O')['position']
        row, col = divmod(best_move, 3)
        board[row][col] = 'O'
    else:
        # Simple AI: choose the first available empty spot on the board
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':  # Check if the cell is empty
                    board[i][j] = 'O'  # Place an 'O' on the board
                    return  # Exit the function after making a move

def is_valid_move(position):
    """
    Validate if the player's move is within the board and the cell is empty.
    """
    row, col = divmod(position-1, 3)
    return board[row][col] == ' '

def next_turn():
    """
    Handle the flow of the game after each move.
    """
    render_board()  # Display the updated board
    result = check_winner()  # Check if there's a winner or a tie
    if result:
        announce_result(result)  # Announce the result
    else:
        global current_player
        if current_player == 'Player':
            current_player = 'Computer'  # Switch to the computer's turn
            get_computer_move()  # Let the computer make a move
            next_turn()  # Continue the game
        else:
            current_player = 'Player'  # Switch to the player's turn
            get_player_move()  # Prompt the player to make a move

def announce_result(result):
    """
    Display the final result of the game and update counters.
    """
    global player_wins, computer_wins, ties
    if result == 'X':  # If the player won
        message = 'Player Wins!'
        player_wins += 1
    elif result == 'O':  # If the computer won
        message = 'Computer Wins!'
        computer_wins += 1
    else:  # If it's a tie
        message = "It's a Tie!"
        ties += 1

    clear_screen()  # Clear the screen to show the result clearly
    green = colors['green']  # Use green color for the message
    reset = colors['reset']  # Reset color to default after the message
    try:
        width = os.get_terminal_size().columns  # Get the width of the console
    except OSError:
        width = 80  # Default to 80 characters if unable to get terminal size
    padding = (width - len(message)) // 2  # Calculate padding to center the message
    print('\n' * 10)  # Add multiple new lines to center the message vertically
    print(' ' * padding + f"{green}{message}{reset}")  # Display the message centered and colored

    # Display current scores
    score_message = f"Scores: Player - {player_wins}, Computer - {computer_wins}, Ties - {ties}"
    padding = (width - len(score_message)) // 2
    print(' ' * padding + f"{colors['green']}{score_message}{colors['reset']}")

    # Save the updated records
    save_records()

    # Ask to play again
    while True:
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again == 'y':
            reset_game()
            break
        elif play_again == 'n':
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def reset_game():
    """
    Reset the game for a new round.
    """
    global board, current_player
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    current_player = 'Player'
    render_board()
    get_player_move()

def minimax(board, player):
    """
    Minimax algorithm for the smart opponent.
    """
    winner = check_winner()
    if winner == 'X':
        return {'score': -1}
    elif winner == 'O':
        return {'score': 1}
    elif winner == 'Tie':
        return {'score': 0}

    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                move = {}
                move['position'] = i * 3 + j
                board[i][j] = player

                if player == 'O':
                    result = minimax(board, 'X')
                    move['score'] = result['score']
                else:
                    result = minimax(board, 'O')
                    move['score'] = result['score']

                board[i][j] = ' '
                moves.append(move)

    best_move = None
    if player == 'O':
        best_score = -float('inf')
        for move in moves:
            if move['score'] > best_score:
                best_score = move['score']
                best_move = move
    else:
        best_score = float('inf')
        for move in moves:
            if move['score'] < best_score:
                best_score = move['score']
                best_move = move

    return best_move

if __name__ == "__main__":
    """
    Start the game by loading records, displaying the empty board, and prompting the player to make the first move.
    """
    try:
        load_records()
        while True:
            choice = input("Do you want to play against a smart opponent? (y/n): ").strip().lower()
            if choice == 'y':
                smart_opponent = True
                break
            elif choice == 'n':
                smart_opponent = False
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        render_board()
        get_player_move()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)