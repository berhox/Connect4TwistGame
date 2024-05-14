# DO NOT modify or add any import statements
from typing import Optional
from a1_support import *

# Name: Hunter Noon
# Student Number: 48819594
# ----------------

# Write your classes and functions here
#The game begins with an empty board of 8 rows separated into 8 columns. Player 1 ( X ) gets to
#make the first move. Until the end of the game, the following steps occur:
#
#   1. The current game board state is displayed.
#
#   2. The user is informed whose turn it is to move.
#
#   3. The user is prompted to enter a command, and then enters one. See Table 1 for the set of
#      valid commands and the actions performed when they are entered. The gameplay/ folder
#      provided with this assignment presents specific examples for what to do on each command.
#
#       Issue with user input                            Constant in a1 support.py
#       The move entered does not begin with a valid     INVALID FORMAT MESSAGE
#       character, the first character is not followed
#       by a single digit integer, or the command
#       contains any superflous characters.
#       The integer is not a valid column on the         INVALID COLUMN MESSAGE
#       board.
#       The move is requesting to add a piece to a       FULL COLUMN MESSAGE
#       full column.
#       The move is requesting to remove a piece         EMPTY COLUMN MESSAGE
#       from an empty column.
#
#    4. If the move is invalid for any reason, the user is shown a message to inform them of why
#      their move was invalid (see Table 2 for all required validity checking and messages for this
#      step), and then the program returns to step 3. If the move is valid, the program progresses
#      to the next step.
#
#   5. The board is updated according to the requested move, and the updated board state is
#      displayed.
#
#   6. If the game is over (Due to either a win or a draw), the program continues to the next step.
#      Otherwise, the program returns to step 1.
#
#    7. When the game is over, the users are informed of the outcome.#
#
#   8. The users are prompted as to whether they would like to play again. At this prompt, if they
#      enter either ‘y’ or ‘Y’, a new game is created (i.e. an empty board is set up and the game
#      returns to player 1’s turn) and the program returns to step 1. If they enter anything other
#      than ‘y’ or ‘Y’, the program should terminate gracefully (that is, the program should end
#      without causing any errors or exiting the test suite).

#Game Functions
def generate_initial_board() -> list[str]:
    """Generates the initial board for the game.
    Preconditions:
        None
    Args:
        None
    Returns:
        list[str]: A list of strings representing the initial state of the game board.
    """
    board = ['--------', '--------', '--------', '--------', '--------', '--------', '--------', '--------']
    return board

def display_board(board: list[str]) -> None:
    """Displays the current state of the game board.
    Preconditions:
        The board is a valid game board. That is, it is a list of strings of length 8.
    Args:
        board (list[str]): A list of strings representing the current state of the game board.
    Returns:
        None   
    """
    for i in range(8):
        row = '|'
        for column in board:
            row = row + column[i] + '|'
        print(row)
    print(' 1 2 3 4 5 6 7 8 ')

def is_column_full(column: str) -> bool:
    """Checks if a column is full.
    Preconditions:
        The column is a valid column of the game board. That is, it is a string of length 8.
        A full column is a column that contains no '-' characters.
    Args:
        column (str): A string representing a column of the game board.
    Returns:
        bool: True if the column is full, False otherwise.
    """
    if '-' not in column:
        return True
    else:
        return False

def is_column_empty(column: str) -> bool:
    """Checks if a column is empty.
    Preconditions:
        The column is a valid column of the game board. That is, it is a string of length 8.
        An empty column is a column that contains only '-' characters.
    Args:  
        column (str): A string representing a column of the game board.
    Returns:
        bool: True if the column is empty, False otherwise.
    """
    if column == '--------':
        return True
    else:
        return False

def num_hours() -> float:
    """Returns the number of hours spent on the assignment.
    Preconditions:
        None
    Args:
        None
    Returns:
        float: The number of hours spent on the assignment.
    """
    hours = 15.0
    return(hours)

def check_input(command: str) -> bool:
    """Checks the validity of the user input with respect to the game's rules.
    Preconditions:
        The command does not violate any game rules
        The user entered column is a single digit number
    Args:
        command (str): A string representing the command entered by the user.
        board (list[str]): A list of strings representing the current state of the game board.
    Returns:
        bool: True if the command is valid, False otherwise.
    """
    #Case where the command is empty, always invalid format!
    if command == "":
        print(INVALID_FORMAT_MESSAGE)
        return False
    #Case where the command is longer than 2 characters, always invalid format!
    elif len(command) > 2:
        print(INVALID_FORMAT_MESSAGE)
        return False
    #Case where the command does not begin with any valid command
    elif command[0].lower() not in ['a', 'r', 'h', 'q']:
        print(INVALID_FORMAT_MESSAGE)
        return False
    #Case where the command is a or r
    elif command[0].lower() == 'a' or command[0].lower() == 'r':
        if len(command) < 2:
            print(INVALID_FORMAT_MESSAGE)
            return False
        elif command[1] not in '12345678':
            print(INVALID_COLUMN_MESSAGE)
            return False
    #Case where the command is h or q
    elif command[0].lower() == 'h' or command[0].lower() == 'q':
        if len(command) > 1:
            print(INVALID_FORMAT_MESSAGE)
            return False
    return True
    
def get_action() -> str:
    """Prompts the user to enter a valid command with respect to the game's rules. When valid command entered, return said command.
    Preconditions:
        None
    Args:
        None
    Returns:
        str: A string representing the command entered by the user.
    """
    while True:
        command = input(ENTER_COMMAND_MESSAGE)
        if check_input(command) == False:
            continue
        else:
            return command

def add_piece(board: list[str], piece: str, column_index: int) -> bool:
    """Adds a piece to the top of a column.
    Preconditions:
        The board represents a valid game state. Additionally, it is a list of strings of length 8.
        The column_index is a valid column index between 0 and 7 inclusive.
    Args:
        board (list[str]): A list of strings representing the current state of the game board.
        piece (str): A string representing the piece to be added to the board.
        column_index (int): An integer representing the column index to add the piece to. This is zero-indexed, column 1 is 0, column 2 is 1, etc.
    Returns:
        bool: True if the piece was successfully added, False otherwise.
    """
    if is_column_full(board[column_index]) == True:
        print(FULL_COLUMN_MESSAGE)
        return False
    else:
        for i in range(len(board[column_index])-1, -1, -1):
            if board[column_index][i] == '-':
                board[column_index] = board[column_index][:i] + piece + board[column_index][i+1:]
                return True
        return False

def remove_piece(board: list[str], column_index: int) -> bool:
    """Removes a piece from the bottom of a column.
    Preconditions:
        The board represents a valid game state. Additionally, it is a list of strings of length 8.
        The column_index is a valid column index between 0 and 7 inclusive.
    Args:
        board (list[str]): A list of strings representing the current state of the game board.
        column_index (int): An integer representing the column index to remove the piece from. This is zero-indexed, column 1 is 0, column 2 is 1, etc.
    Returns:
        bool: True if the piece was successfully removed, False otherwise.
    """
    if is_column_empty(board[column_index]) == True:
        print(EMPTY_COLUMN_MESSAGE)
        return False
    else:
        # Convert the string to a list
        column = list(board[column_index])
        for row_index in range(len(column)-1, -1, -1):
            if column[row_index] != '-':
                # Shift all pieces above down
                for shift_row_index in range(row_index, 0, -1):
                    column[shift_row_index] = column[shift_row_index-1]
                # Replace the top piece with '-'
                column[0] = '-'
                # Convert the list back to a string and store it back into the board
                board[column_index] = ''.join(column)
                return True
        return False


def check_win(board):
    """Checks if a player has won the game.
    Preconditions:
        The board represents a valid game state. Additionally, it is a list of strings of length 8.
            The piece is a valid game piece. That is, it is a string of length 1.
    Args:
        board (list[str]): A list of strings representing the current state of the game board.
    Returns:
        Optional[str]: The piece that has won the game, or None if no player has won.
    """
    EMPTY = '-' 
    player1_win = False
    player2_win = False
    # Check for horizontal win
    for row in range(8):
        for col in range(5):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] != EMPTY:
                if board[row][col] == 'X':
                    player1_win = True
                else:
                    player2_win = True

    # Check for vertical win
    for row in range(5):
        for col in range(8):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] != EMPTY:
                if board[row][col] == 'X':
                    player1_win = True
                else:
                    player2_win = True

    # Check for diagonal win
    for row in range(5):
        for col in range(5):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] != EMPTY:
                if board[row][col] == 'X':
                    player1_win = True
                else:
                    player2_win = True

    for row in range(5):
        for col in range(7, 2, -1):
            if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] != EMPTY:
                if board[row][col] == 'X':
                    player1_win = True
                else:
                    player2_win = True

    # Check for draw
    if player1_win and player2_win:
        return '-'
    
    # If no draw, return the winner (or None if there's no winner yet)
    if player1_win:
        return 'X'
    if player2_win:
        return 'O'
    return None
    


def play_game() -> str:
    """Plays a game of connect 4.
    Preconditions:
        None
    Args:
        None
    Returns:
        str: The outcome of the game. 'X' if player 1 wins, 'O' if player 2 wins, 'draw' if the game is a draw, and 'quit' if the user quits the game.
    """
    board = generate_initial_board()
    player = PLAYER_1_PIECE
    outcome = None
    display_board(board)
    while True:
        if player == PLAYER_1_PIECE:
            print(PLAYER_1_MOVE_MESSAGE)
        else:
            print(PLAYER_2_MOVE_MESSAGE)
        while True:
            command = get_action()
            if command[0].lower() == 'a':
                if add_piece(board, player, int(command[1])-1) == False:
                    continue
                else:
                    display_board(board)
                    break
            elif command[0].lower() == 'r':
                if remove_piece(board, int(command[1])-1) == False:
                    continue
                else:
                    display_board(board)
                    break
            elif command[0].lower() == 'h':
                print(HELP_MESSAGE)
                display_board(board)
                if player == PLAYER_1_PIECE:
                    print(PLAYER_1_MOVE_MESSAGE)
                else:  
                    print(PLAYER_2_MOVE_MESSAGE)
                continue
            elif command[0].lower() == 'q':
                return 'quit' # type: ignore
        outcome = check_win(board)
        if outcome == PLAYER_1_PIECE:
            print(PLAYER_1_VICTORY_MESSAGE)
            return 'X' # type: ignore
        elif outcome == PLAYER_2_PIECE:
            print(PLAYER_2_VICTORY_MESSAGE)
            return 'O' # type: ignore
        elif outcome == '-':
            print(DRAW_MESSAGE)
            return 'draw' # type: ignore
        if player == PLAYER_1_PIECE:
            player = PLAYER_2_PIECE
        else:
            player = PLAYER_1_PIECE

#The Game
def main() -> None:
    """The main function that is run when the program is executed. It enacts a game of connect 4.
    Preconditions:
        None
    Args:
        None
    Returns:
        Begins the game when program is run
    """
    while True:
        outcome = play_game()
        if outcome is not None:
            play_again_quiz = input(CONTINUE_MESSAGE)
            if play_again_quiz.lower() != 'y':
                break

if __name__ == "__main__":
    main()

