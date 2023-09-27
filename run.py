import gspread
from google.oauth2.service_account import Credentials

# Initialize Google Sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Elves-and-Dwarfs')

Stats = SHEET.worksheet('Stats')

# Character class selection
print("Welcome to The Mighty Land of Elves and Dwarves!")
print("Choose your starting class:")
print("1. Elf")
print("2. Dwarf")
class_choice = input("Enter the number of your choice: ")

# Customized character name
character_name = input("Enter your character's name: ")

# Initialize character stats
if class_choice == "1":
    character_class = "Elf"
    health = 100
    strength = 10
elif class_choice == "2":
    character_class = "Dwarf"
    health = 120
    strength = 8

# Game loop
while True:
    # Display game storyline and choices
    print("\nChapter 1: The Enchanted Forest")
    print(f"{character_name}, you find yourself in the heart of an enchanted forest, surrounded by towering trees and mystical creatures.")
    print("As you walk deeper into the forest, you encounter a massive tree blocking your path.")
    print("1. Choose to walk around the tree.")
    print("2. Decide to take on the challenge and try to get rid of the tree.")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("You decide to take the safe route and walk around the tree.")
        # No change in stats
        pass
    elif choice == "2":
        print(f"You summon your {character_class}'s courage and attempt to get rid of the tree. The effort grants you +1 strength.")
        strength += 1

    # Update character info in the spreadsheet
    worksheet.append_row([character_name, character_class, health, strength])

    # Check if the player is strong enough to face the boss
    if strength >= 10:
        print("\nChapter 2: The Final Battle")
        print("You face the mighty boss!")
        boss_health = 20
        boss_strength = 10

        while boss_health > 0:
            # Combat logic here
            # You can implement combat mechanics like attacking, defending, etc.
            pass

        if boss_health <= 0:
            print("Congratulations! You defeated the boss and won the game!")
        else:
            print("You were defeated by the boss. Game over.")
        break

# End the game
print("Thank you for playing The Mighty Land of Elves and Dwarves!")