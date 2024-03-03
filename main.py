from utils import *


def main():
    # Welcome
    print("Welcome to the game of 'Odd or Even?'")
    
    # Perform the toss and get the batting player
    defending_batter_id = perform_toss_and_get_batter_id()
    batter_name = get_player_corresponding_to_id(defending_batter_id)

    # Start the round and set a target score for the chasing player to chase
    target_score = play_round_and_get_batter_score(defending_batter_id)

    # Chasing batter will be the opposite of the defending. If defending = 0 then chasing = 1 and vice-versa
    chasing_batter_id = 0 if defending_batter_id == 1 else 1
    chasing_batter_name = get_player_corresponding_to_id(chasing_batter_id)

    # Print info
    print(f"The first batter has scored: {target_score}")
    print(f"The second (chasing) batter has to score {target_score + 1} to win the game.")
    print("Let the chase begin!")

    # Start the chasing round and get the score of the chasing player
    chasing_score = play_round_and_get_batter_score(chasing_batter_id, chasing_round=True, score_to_chase=target_score)
    print_sep()

    # Decide the winner by comparing the chasing score and the target score
    if chasing_score > target_score:
        winner = chasing_batter_name.upper()
        print(f"The target score was: {target_score}")
        print(f"The chasing player scored {chasing_score} and successfully won the game!")
        print(f"{winner} has won the game.")
    else:
        print(f"The target score was: {target_score}")
        print(f"The chasing player only scored {chasing_score} and lost the game!")
        winner = batter_name.upper()
        print(f"{winner} has won the game.")


if __name__ == "__main__":
    main()
