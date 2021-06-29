# constant variables
max_stones_global = 5
total_stones_global = 100


def game(total_stones, max_stones):
    """
    This is an interactive two-player game called Nims and Stone. Each player can draw between 1 and a
    maximum number of stones from global max_stones, calling on the validity_check function to check if the move
    is allowed. The game will keep on going until the last stone is drawn,
    declaring the winner.

    :param total_stones: total amount of stones the players have to draw from
    precondition: must be an integer

    :param max_stones: maximum number of stones the players can draw each turn
    precondition: must be an integer

    :return: the winner of the game according to the last stone taken (player 1 or player 2)
    """

    pile = total_stones
    print("There are", total_stones, "stones.")
    print("You can take a maximum of", max_stones, "stones each turn.")

    while pile > 0:
        # player one's turn
        player = 1
        while player == 1 and pile > 0:
            player_one_move = int(input("Player 1: What's your move? "))

            # checks if move is valid
            if 0 < player_one_move <= max_stones:
                potential_remaining = pile - player_one_move

                # logical conditions for game to continue or end
                # potential_remaining subtracts from pile if player move is valid given remaining stones
                if potential_remaining == 0:
                    print("Player 1 wins!")
                elif potential_remaining < 0:
                    print("Sorry, try again. You can't have a negative number of stones.")
                    continue
                elif potential_remaining > 0:
                    player = 2
                pile -= player_one_move
                print("Total stones left:", pile)

            else:
                print("Sorry, try again.")
                player = 1

        # player two's turn
        while player == 2 and pile > 0:
            player_two_move = int(input("Player 2: What's your move? "))

            # checks if move is valid
            if 0 < player_two_move <= max_stones:
                potential_remaining = pile - player_two_move

                # conditions for game to continue or end
                # potential_remaining subtracts from pile if player move is valid given remaining stones
                if potential_remaining == 0:
                    print("Player 2 wins!")
                elif potential_remaining < 0:
                    print("Sorry, try again. You can't have a negative number of stones.")
                    continue
                elif potential_remaining > 0:
                    player = 1
                pile -= player_two_move
                print("Total stones left:", pile)

            else:
                print("Sorry, try again.")
                player = 2


game(total_stones_global, max_stones_global)
