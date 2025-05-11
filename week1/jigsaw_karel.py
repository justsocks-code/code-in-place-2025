from karel.stanfordkarel import *

# File: jigsaw_karel.py
# -----------------------------
# Challenge: Jigsaw Karel
# Karel picks up a beeper (puzzle piece),
# places it in the final puzzle spot,
# and returns to the starting point.

def main():
    pick_up_piece()
    place_piece()
    return_home()

def pick_up_piece():
    while no_beepers_present():
        move()
    pick_beeper()

def place_piece():
    move()
    turn_left()
    move()
    move()
    put_beeper()

def return_home():
    turn_around()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_around()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

# Don't edit below this line
if __name__ == '__main__':
    main()

