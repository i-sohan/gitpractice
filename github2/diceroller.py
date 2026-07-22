#Dice roller game
import random

print("🎲 Welcome to the Dice Roller!")

while True:
    input("\nPress Enter to roll the dice...")

    dice = random.randint(1, 6)

    print(f"You rolled: {dice}")

    choice = input("Roll again? (y/n): ").lower()

    if choice != "y":
        print("\nThanks for playing! 👋")
        break
