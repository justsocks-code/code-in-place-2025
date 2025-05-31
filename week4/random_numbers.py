# File: random_numbers.py
# -----------------------------
# Generates and prints a series of random integers
# between MIN_VALUE and MAX_VALUE using a for loop.

import random

# Constants
N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    for i in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))

# Required to run the main function
if __name__ == '__main__':
    main()
