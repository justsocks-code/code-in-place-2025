# File: the_game_of_nimm.py
# -----------------------------
# Two-player version of the Game of Nimm.
# Whoever takes the last stone loses.

TOTAL_STONES = 20

def main():
    stones = TOTAL_STONES
    player = 1

    while stones > 0:
        print(f"There are {stones} stones left.")
        move = get_valid_move(player, stones)
        stones -= move
        print()  # Blank line after move prompt

        if stones == 0:
            
            other_player = 2 if player == 1 else 1
            print(f"Player {other_player} wins!")
            break

        player = 2 if player == 1 else 1

def get_valid_move(player, stones_left):
    prompt = f"Player {player} would you like to remove 1 or 2 stones?  "
    while True:
        move = input(prompt)
        if move.strip() in ['1', '2']:
            move = int(move)
            if move <= stones_left:
                return move
        prompt = "Please enter 1 or 2:  "

if __name__ == '__main__':
    main()
