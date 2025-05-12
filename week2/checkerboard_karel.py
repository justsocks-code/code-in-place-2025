from karel.stanfordkarel import *

# File: checkerboard_karel.py
# -----------------------------
# Challenge: Checkerboard Karel
# Karel places beepers in a checkerboard pattern across
# a world of unknown size and ends up in the bottom-left
# corner facing east.

def main():
    # Fill the first row
    row_check()

    # Move up to second row, offset pattern depending on first tile
    if beepers_present():
        turn_left()
        move()
        turn_left()
        if front_is_clear():
            move()
            row_check_2()  # Start checkerboard pattern offset by 1
    else:
        turn_left()
        move()
        turn_left()
        row_check_2()

    # Prepare to continue zigzag pattern
    turn_left()
    turn_left()
    turn_left() 

    while front_is_clear():
        move()

        # If we can go up another row
        if left_is_clear():
            turn_around()

        if no_beepers_present():
            row_check()

            # Try to move up if possible
            if front_is_clear():
                move()

            # Depending on where the last beeper was, decide offset
            if beepers_present():
                turn_around()
                move()
                turn_left()
                while front_is_clear():
                    move()
                    row_check_2()
            else:
                turn_left()
                move()
                turn_left()
                row_check_2()

            # Turn to prepare for next zigzag
            turn_left()
            turn_left()
            turn_left() 

    # Return to starting position: bottom-left corner facing east
    while not_facing_south():
        turn_left()
    while front_is_clear():
        move()
    while not_facing_west():
        turn_left() 
    while front_is_clear():
        move()       
    while not_facing_east():
        turn_left()

# Places beepers in every other tile from left to right
def row_check():
    put_beeper()
    while not_facing_east():
        turn_left()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

# Offset version of row_check for alternating rows
def row_check_2():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

# Helper to turn around (180°)
def turn_around():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
