from karel.stanfordkarel import *

# File: stone_mason_karel.py
# -----------------------------
# Challenge: Stone Mason Karel
# Karel builds vertical columns by placing missing beepers
# every 4th column in a world that is 5 units tall.

def main():
    # There are 4 columns to repair
    for _ in range(4):
        build_column()
        if front_is_clear():
            move_to_next_column()

def build_column():
    turn_left()
    for _ in range(4):
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()
    turn_around()
    for _ in range(4):
        move()
    turn_left()

def move_to_next_column():
    for _ in range(4):
        move()

def turn_right():
    for _ in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

# Don't edit below this line
if __name__ == '__main__':
    main()
