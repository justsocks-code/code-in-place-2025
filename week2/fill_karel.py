from karel.stanfordkarel import *

# File: fill_karel.py
# -----------------------------
# Challenge: Fill Karel
# Karel fills each row with beepers in a zigzag pattern.
# After completing a row, she returns to the start,
# moves up to the next row (if possible), and continues.

def main():
    # Keep working as long as the current tile has no beeper,
    # which is our way of checking if there's still work to do.
    while no_beepers_present():
        fill()         # Fill the current row with beepers
        return()     # Return to the start of the row
        if front_is_clear():
            move()         # Move up to next row (1 tile upward)
            turn_right()   # Turn to face correct direction
        else:
            turn_right()           # At top row: rotate
            while front_is_clear():  # Move to the wall to finish
                move()

def fill():
    # Fills the current row with beepers
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

def return():
    # Goes back to the start of the current row
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_right()

def turn_right():
    # Helper function to turn right
    turn_left()
    turn_left()
    turn_left()

# Don't edit below this line
if __name__ == '__main__':
    main()
