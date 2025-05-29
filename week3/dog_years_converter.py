# File: dog_years_converter.py
# -----------------------------
# Converts human calendar years to dog years using a fixed multiplier.

DOG_YEARS_MULTIPLIER = 7.18  # Each human year is roughly 7.18 dog years

def main():
    years = float(input("Enter an age in calendar years: "))
    dog_years = years * DOG_YEARS_MULTIPLIER
    print(f"That's {dog_years} in dog years!")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
