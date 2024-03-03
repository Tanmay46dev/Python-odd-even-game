import random

# List of all the allowed moves
ALLOWED_MOVES = ["1", "2", "3", "4", "5", "6", "10"]


def print_sep():
    print("---------------------------------------------------------------------------")


def get_player_corresponding_to_id(player_id: int) -> str:
    """
    :param player_id: The id of the concerned player
    :return: "player" if player_id is 0, otherwise returns "cpu"
    """
    if player_id == 0:
        return "user"
    else:
        return "cpu"


def perform_toss_and_get_batter_id() -> int:
    """
    Performs a toss and returns the batter_id of the player who is batting first
    :return: batter_id
    """
    while True:
        call = input("Odd or Even?\nEnter your choice: ")
        if call == "odd" or call == "even":
            cpu_move = get_random_move()
            player_move = get_user_move()
            print(f"You played: {player_move} and the CPU played {cpu_move}")
            if player_won_toss(player_move, cpu_move, call):
                while True:
                    choice = input("Congrats! You have won the toss. Would you like to 'bat' or 'bowl' first?: ")
                    if choice == "bat":
                        return 0
                    elif choice == "bowl":
                        return 1
                    print("Invalid choice. Please try again!")
            else:
                print("Ohh! You have lost the toss!")
                cpu_choice = random.choice(["bat", "bowl"])
                print(f"The CPU won the toss and chose to '{cpu_choice}' first. Good luck!")
                if cpu_choice == "bat":
                    return 1
                else:
                    return 0
        else:
            print("Invalid call. Please try again!")


def player_won_toss(user_move: int, cpu_move: int, call: str) -> bool:
    """

    :param user_move: The move of the user
    :param cpu_move: The move of the cpu
    :param call: The call of the user (even or odd)
    :return: True if player has won the toss, else False
    """
    move_sum = user_move + cpu_move

    return "even" if move_sum % 2 == 0 else "odd" == call


def get_random_move() -> int:
    """
    :return: A random move from the list of allowed moves
    """
    return int(random.choice(ALLOWED_MOVES))


def get_user_move() -> int:
    while True:
        print_sep()  # Print a seperator
        [print(move, end=" ") for move in ALLOWED_MOVES]
        print()
        player_move = input("Enter a move from the choices above: ")
        if player_move in ALLOWED_MOVES:
            return int(player_move)
        print("Invalid move. Please try again!")


def play_round_and_get_batter_score(batter_id: int, chasing_round=False, score_to_chase: int = 0) -> int:
    batter_score = 0
    print_sep()
    print(get_player_corresponding_to_id(batter_id).upper() + " is currently batting.")
    while True:
        cpu_move = get_random_move()
        user_move = get_user_move()

        print_sep()
        print(f"You played {user_move} and the CPU played {cpu_move}")
        print_sep()

        if cpu_move == user_move:
            break

        if batter_id == 0:
            batter_score += user_move
        else:
            batter_score += cpu_move

        print(f"Batter's current score: {batter_score}")
        if chasing_round:
            if batter_score > score_to_chase:
                break

    return batter_score
