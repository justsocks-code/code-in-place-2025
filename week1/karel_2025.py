from karel.stanfordkarel import *

# File: karel_2025.py
# -----------------------------
# Challenge: 2025 Karel
# Karel places two piles of beepers to celebrate:
# - 20 beepers on one square
# - Then moves and places 25 more
# Then she moves one last time to finish.

def main():
    put_beeper_pile(20)
    move()
    put_beeper_pile(25)
    move()

def put_beeper_pile(count):
    for i in range(count):
        put_beeper()

# Don't edit below this line
if __name__ == '__main__':
    main()
