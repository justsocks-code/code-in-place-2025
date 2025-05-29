# File: multiply_two_numbers.py
# -----------------------------
# A simple Python program that multiplies two numbers
# entered by the user and prints the result.

def main():
    print("This program multiplies two numbers.")

    # Get user input and convert to integers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Perform multiplication
    result = num1 * num2

    # Print the result
    print("The result is:", result)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
