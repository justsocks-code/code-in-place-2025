# File: hailstone.py
# -----------------------------
# Prompts the user for a positive integer and applies the
# Hailstone sequence until the number reaches 1.

def main():
    hailstone_sequence()

def hailstone_sequence():
    n = int(input("Enter a number: "))
    steps = 0

    while n != 1:
        if n % 2 == 0:
            print(f"{n} is even, so I take half: {n // 2}")
            n = n // 2
        else:
            print(f"{n} is odd, so I make 3n + 1: {3 * n + 1}")
            n = 3 * n + 1
        steps += 1

    print(f"That took {steps} steps to reach 1.")

# Required line to run the program
if __name__ == "__main__":
    main()
