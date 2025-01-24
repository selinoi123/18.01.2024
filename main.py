from memory_game import game_start_confirmation, choosing_the_number_of_players, function_name_selection, cards_memory, turn_play

game_start_confirmation()
game_mode = choosing_the_number_of_players()
player1_name, player2_name = function_name_selection(game_mode)
array_two, array = cards_memory()

if __name__ == '__main__':

    print("Great, you can start the game!")
    print("If you want to restart the game, press 'R'.")
    print("This is the memory game board:")

    array = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"]
    ]

    print("--------------------------------")
    for row in array:
        print(" ".join(row))
    print("--------------------------------")


    turn_play(array_two, array, player1_name, player2_name)


