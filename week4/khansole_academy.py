# File: khansole_academy.py
# -----------------------------
# Simulates a math drill from Khansole Academy.
# Randomly generates two-digit addition problems
# and checks if the user's answer is correct.

import random

def main():
    print("Khansole Academy")

    # Generate two random two-digit numbers
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)

    # Prompt the user with an addition problem
    print(f"What is {num1} + {num2}?")
    answer = int(input("Your answer: "))

    # Check the result
    if answer == num1 + num2:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The expected answer is", num1 + num2)

# Required line to execute main()
if __name__ == '__main__':
    main()
