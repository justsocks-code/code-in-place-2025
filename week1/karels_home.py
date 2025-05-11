from karel.stanfordkarel import *

# File: karels_home.py
# -----------------------------
# Challenge: Karel's Home
# Karel moves out of the house, picks up a beeper,
# and returns to her original position.

def main():
    go_to_beeper()
    pick_beeper()
    return_home()

def go_to_beeper():
    move()
    move()
    turn_left()
    move()

def return_home():
    turn_around()
    move()
    turn_right()
    move()
    move()
    turn_around()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

# Don't edit these next two lines — they make sure main() runs.
if __name__ == '__main__':
    main()
