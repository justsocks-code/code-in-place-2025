# File: sunrise_fill_in.py
# -----------------------------
# A fill-in-the-blank storytelling prompt.
# The user is asked to provide a color, an adjective,
# and a goal — then the program generates a poetic sentence.

def main():
    color = input("A color: ")
    adjective = input("An adjective: ")
    goal = input("A goal you would like to achieve: ")
    
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")

if __name__ == "__main__":
    main()
