from karel.stanfordkarel import *

# File: beeper_path.py
# -----------------------------
# Challenge: Beeper Path
# Karel follows a trail of beepers
# and moves one step past the end of the path.

def main():
    while beeper_present():
        move()

# Don't edit below this line
if __name__ == '__main__':
    main()
