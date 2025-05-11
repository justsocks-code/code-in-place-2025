from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# Challenge: Piles
# Karel moves along the first row,
# picking up all the beepers in each square.

def main():
    while front_is_clear():
        clean_pile()
        move()
    # Clean final square if it has beepers
    clean_pile()

def clean_pile():
    while beepers_present():
        pick_beeper()

# Don't edit below this line
if __name__ == '__main__':
    main()
