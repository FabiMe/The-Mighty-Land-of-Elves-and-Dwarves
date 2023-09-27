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

# Initialize a variable to track whether the first chapter has been completed
first_chapter_completed = False
second_chapter_completed = False
third_chapter_completed = False
fourth_chapter_completed = False

# Game loop
while True:
    # Display game storyline and choices for Chapter 1
    if not first_chapter_completed:
        print("\nChapter 1: The Enchanted Forest")
        print(f"{character_name}, you find yourself in the heart of an enchanted forest, surrounded by towering trees and mystical creatures.")
        print("As you walk deeper into the forest, you encounter a massive tree blocking your path.")
        print("1. Choose to walk around the tree. (+1 Health)")
        print("2. Decide to take on the challenge and try to get rid of the tree. (+1 Strength)")

        # Input validation loop for Chapter 1
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice in ["1", "2"]:
                break
            else:
                print("To continue your journey you must follow the rules. Choose 1 or 2.")

        if choice == "1":
            print("You decide to take the safe route and walk around the tree, improving your health.")
            health += 1
        elif choice == "2":
            print(f"You summon your {character_class}'s courage and attempt to get rid of the tree, gaining strength.")
            strength += 1

        # Add a new row with character stats for the first chapter
        character_stats = [character_name, character_class, health, strength]
        Stats.insert_rows([character_stats], 2, value_input_option='RAW')  # Insert the row at row 2

        first_chapter_completed = True
    else:
        # Display game storyline and choices for Chapter 2
        if first_chapter_completed and not second_chapter_completed:
            print("\nChapter 2: The Mysterious Glowing Orb")
            print("As you journey further, you stumble upon a clearing bathed in an eerie, otherworldly light.")
            print("In the center, you notice a mysterious glowing orb.")
            print("1. Reach out and touch the orb.")
            print("2. Proceed cautiously around the orb.")

            # Input validation loop for Chapter 2
            while True:
                choice = input("Enter your choice (1 or 2): ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("To continue your journey you must follow the rules. Choose 1 or 2.")

            if choice == "1":
                print("You reach out and touch the glowing orb, you feel a charge in your body. It feels dark and cold. (-2 Health)")
                health -= 2
            elif choice == "2":
                print("You proceed cautiously around the orb, ensuring your safety and health. (Health +1)") 
                health += 1

                # Update character stats in Google Sheets
                updated_stats = [character_name, character_class, health, strength]
                Stats.update('A2', [updated_stats])  # Update character stats starting from cell 'A2'
            
            second_chapter_completed = True

        # Display game storyline and choices for Chapter 3
        elif second_chapter_completed and not third_chapter_completed:
            print("\nChapter 3: The Haunted Castle")
            print("As you continue your journey, you come across a looming, ancient castle surrounded by a thick fog.")
            print("Curiosity gets the better of you, and you decide to explore the castle.")
            print("1. Enter the castle's grand hall.")
            print("2. Search the castle's perimeter for another entrance.")

            # Input validation loop for Chapter 3
            while True:
                choice = input("Enter your choice (1 or 2): ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("To continue your journey you must follow the rules. Choose 1 or 2.")

            if choice == "1":
                print("You boldly enter the castle's grand hall, but the doors slam shut behind you. The castle is haunted! (-3 Health)")
                health -= 3
            elif choice == "2":
                print("You cautiously search the castle's perimeter and find a hidden entrance, avoiding the haunted grand hall. (Health +2)")
                health += 2

                # Update character stats in Google Sheets
                updated_stats = [character_name, character_class, health, strength]
                Stats.update(value=[updated_stats], range_name='A2')  # Update character stats starting from cell 'A2'

            third_chapter_completed = True

        # Display game storyline and choices for Chapter 4
        elif third_chapter_completed and not fourth_chapter_completed:
            print("\nChapter 4: The Dragon's Lair")
            print("Deep within the castle, you discover a hidden chamber. At the center of the chamber lies a slumbering dragon.")
            print("1. Attempt to sneak past the dragon and continue your quest.")
            print("2. Wake up the dragon to face it head-on.")

            # Input validation loop for Chapter 4
            while True:
                choice = input("Enter your choice (1 or 2): ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("To continue your journey you must follow the rules. Choose 1 or 2.")

            if choice == "1":
                print("You silently tiptoe past the dragon, avoiding a fiery confrontation. (Strength +2)")
                strength += 2
            elif choice == "2":
                print("You awaken the dragon, and a fierce battle ensues. You emerge victorious but wounded. (-4 Health)")
                health -= 4
                strength += 1

                # Update character stats in Google Sheets
                updated_stats = [character_name, character_class, health, strength]
                Stats.update(value=[updated_stats], range_name='A2')  # Update character stats starting from cell 'A2'

            fourth_chapter_completed = True