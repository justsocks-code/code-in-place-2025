from karel.stanfordkarel import *

# File: midpoint_karel.py
# -----------------------------
# Challenge: Midpoint Karel
# Karel places a beeper at the midpoint of the 1st street.
# Any temporary beepers used during the process must be cleaned up.

def main():
    # Step 1: Place beeper at both ends of the row
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    
    # Step 2: Begin shrinking toward the center
    turn_around()
    move()
    while no_beepers_present():
        move()
        while no_beepers_present():
            move()
        shift_beeper_inward()
        move()

    # Step 3: Clean up all extra beepers except the middle one
    while beepers_present():
        if facing_west():
            turn_around()
            move()
            if right_is_clear():
                move()
                pick_beeper()
            else:
                pick_beeper()
        else:
            pick_beeper()

    # Step 4: Move Karel to stand on the final midpoint beeper
    while no_beepers_present():
        turn_around()
        move()
    turn_around()

# Helper function: move one beeper inward
def shift_beeper_inward():
    turn_around()
    pick_beeper()
    move()
    put_beeper()

# Helper function: turn 180 degrees
def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
