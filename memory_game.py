import random

"""
     get_integer_input - A function that checks the input type and checks if an integer has been entered,
     if not it sends a Error. In short, the function handles errors.
"""
def get_integer_input(prompt) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


"""
     game_start_confirmation - The function is designed to get permission
     from the user to start the game.
"""

def game_start_confirmation():
    print('Welcome to the "Memory Game".')
    print("Type 1 so we can proceed.")
    while get_integer_input("Enter 1 to proceed: ") != 1:
        print("Invalid input! Please enter the number 1.")
    print("Game will start now!")

"""
     choosing_the_number_of_players - The function will allow the user to choose a game mode:
     play against another player or against the computer.
"""

def choosing_the_number_of_players():
    game_mode = get_integer_input("Enter 1 to play against another player or 2 to play against the computer: ")
    while game_mode not in [1, 2]:
        print("Invalid input! Please enter 1 or 2.")
        game_mode = get_integer_input("Enter 1 to play against another player or 2 to play against the computer: ")
    return game_mode


"""
     function_name_selection - The function is designed to determine the name
     of the players according to the state of the game.
"""

def function_name_selection(game_mode : int):
    player1_name = input("Player1: enter your name: ")
    if game_mode == 1:
        player2_name = input("Player2: enter your name: ")
        return player1_name, player2_name
    else:
        return player1_name, "Computer"


"""
     cards_memory - The function is designed to prepare the board 
     for a memory game where the cards are matching pairs.
"""

def cards_memory():
    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F']
    random.shuffle(cards)

    array = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"]
    ]

    array_two = [row[:] for row in array]

    c = 0
    for i in range(3):
        for j in range(4):
            array_two[i][j] = cards[c]
            c += 1
    return array_two, array


"""
     print_board - The role of the function is to display the game board
     in an orderly and aesthetic way, when each line in the array (board) is printed in a separate line.
"""

def print_board(array : list):
    print("--------------------------------")
    for row in array:
        print(" ".join(row))
    print("--------------------------------")

"""
     computer_select_card - The function allows the computer to take turns playing a memory game,
     choosing a hidden card at random or revealing .
"""

def computer_select_card(array : list, array_two : list):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 3)
        if array[row][col] == "X":
            array[row][col] = array_two[row][col]
            print(f"Computer chose row {row}, column {col}.")
            return row, col


"""
     turn_play - The function is designed to manage the course of the game in turns between two players
     (or a player and the computer), including choosing cards, 
     checking matches and managing the turn of the players until the end of the game.
     and says who won the game or that the game ended in a draw.
     It also asks the user if they want to play another game
"""


def turn_play(array_two : list, array : list, player1_name : str, player2_name : str):
    turn = player1_name
    player1_pairs = 0
    player2_pairs = 0

    while True:
        print(f"{turn}'s turn.")

        if turn == "Computer":
            print("Computer is choosing...")
            first_card = computer_select_card(array, array_two)
            second_card = computer_select_card(array, array_two)
        else:
            first_card = select_card(array, array_two)
            second_card = select_card(array, array_two)

        if array_two[first_card[0]][first_card[1]] == array_two[second_card[0]][second_card[1]]:
            print(f"{turn} found a match!")
            if turn == player1_name:
                player1_pairs += 1
            elif turn == player2_name:
                player2_pairs += 1
        else:
            print(f"{turn} did not find a match.")
            array[first_card[0]][first_card[1]] = "X"
            array[second_card[0]][second_card[1]] = "X"

        print_board(array)

        if turn == player1_name:
            turn = player2_name
        else:
            turn = player1_name

        if game_over(array):
            print("Game Over!")
            break

    print(f"{player1_name} found {player1_pairs} pairs.")
    print(f"{player2_name} found {player2_pairs} pairs.")

    if player1_pairs > player2_pairs:
        print(f"{player1_name} wins!")
    elif player2_pairs > player1_pairs:
        print(f"{player1_name} wins!")
    else:
        print("The game ended in a draw")

    replay = input("Play another game? Enter '1' for yes, any other key to exit: ")
    if replay == "1":
        array_two, array = cards_memory()
        turn_play(array_two, array, player1_name, player2_name)
    else:
        print("Thanks for playing! Goodbye!")

"""
     select_card - The function allows the player to choose a card in a safe way 
     and checks the correctness of the input. This ensures that the player does not
     choose another revealed card and does not choose outside the board boundaries.
"""

def select_card(array : list, array_two : list):
    while True:
        row = get_integer_input("Enter the row (0, 1, 2): ")
        col = get_integer_input("Enter the column (0, 1, 2, 3): ")
        if 0 <= row < 3 and 0 <= col < 4:
            if array[row][col] == "X":
                array[row][col] = array_two[row][col]
                return row, col
            else:
                print("That spot is already revealed. Choose again.")
        else:
            print("Invalid position. Please enter valid coordinates.")


"""
     game_over- The function checks if all cards have been revealed during the game
     It is used to determine if the game is over, and returns true if all cards have been revealed and false if not.
"""

def game_over(array : list):
    for row in array:
        if "X" in row:
            return False
    return True








