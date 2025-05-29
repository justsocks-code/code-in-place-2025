# File: haiku_generator.py
# -----------------------------
# Generates a custom haiku using GPT, based on the user's name and topic.

from ai import call_gpt  # Assumes you have a custom wrapper for GPT API

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")

    print("Creating your haiku...")

    # Prompt GPT to generate a haiku with name and topic
    haiku = call_gpt(
        f"Write a haiku inspired by {topic} and include {name}. "
        "Don't include any explanations, just return the haiku in three lines."
    )

    print("\n" + haiku)

if __name__ == "__main__":
    main()
