import gspread
import time
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

# ANSI escape codes for text formatting
GREEN_TEXT = "\033[32m"
BLACK_BACKGROUND = "\033[40m"
ITALIC = "\033[3m"
RESET_FORMATTING = "\033[0m"

# Function to find the row index of a character in the spreadsheet
def find_character_row(character_name):
    Stats = SHEET.worksheet('Stats')
    values = Stats.get_all_values()
    for i, row in enumerate(values):
        if row and row[0] == character_name:
            return i + 1  # Return the row index (1-based)
    return None  # Character row not found

# Function to create a new row with character data in the spreadsheet
def create_character_row(character_name, character_class, health, strength):
    Stats = SHEET.worksheet('Stats')
    character_stats = [character_name, character_class, health, strength]
    Stats.append_rows([character_stats], value_input_option='RAW')

# Function to update character's Health and Strength in the spreadsheet
def update_character_stats(character_name, health, strength):
    Stats = SHEET.worksheet('Stats')
    row_index = find_character_row(character_name)
    
    if row_index is not None:
        # Character row exists, fetch existing data and update Health and Strength
        existing_data = Stats.row_values(row_index)
        existing_data[2] = health  # Update Health
        existing_data[3] = strength  # Update Strength
        Stats.update(f"A{row_index}:D{row_index}", [existing_data], value_input_option='RAW')

# Function to transfer character data to the "Hall of Fame" sheet
def transfer_to_hall_of_fame(character_name, character_class, health, strength):
    Stats = SHEET.worksheet('Stats')
    HallOfFame = SHEET.worksheet('Hall of Fame')
    character_stats = [character_name, character_class, health, strength]

    # Find the character's row in the "Stats" sheet
    row_index = find_character_row(character_name)

    if row_index is not None:
        # Copy the character's data to the "Hall of Fame" sheet
        HallOfFame.append_rows([character_stats], value_input_option='RAW')

        # Delete the character's row from the "Stats" sheet
        Stats.delete_row(row_index)

# Character class selection
print(f"{GREEN_TEXT}{BLACK_BACKGROUND}")
print("Welcome to The Mighty Land of Elves and Dwarves!")
print("Choose your starting class:")
print("1. Elf")
print("2. Dwarf")
class_choice = input("Enter the number of your choice: ")

# Customized character name
character_name = input(f"{ITALIC}Enter your character's name: ")

# Initialize character's stats
if class_choice == "1":
    character_class = "Elf"
    health = 40
    strength = 2
elif class_choice == "2":
    character_class = "Dwarf"
    health = 20
    strength = 4

# Create a new row with character data in the spreadsheet
create_character_row(character_name, character_class, health, strength)

#Initialize a variable to track whether the actual chapter is completed
first_chapter_completed = False
second_chapter_completed = False
third_chapter_completed = False
fourth_chapter_completed = False
fifth_chapter_completed = False
sixth_chapter_completed = False
seventh_chapter_completed = False
eighth_chapter_completed = False
ninth_chapter_completed = False
tenth_chapter_completed = False
eleventh_chapter_completed = False
twelfth_chapter_completed = False
all_chapters_completed = False

# Game loop
while not all_chapters_completed:
    # Display game storyline and choices for Chapter 1
    if not first_chapter_completed:
        print(f"{GREEN_TEXT}{BLACK_BACKGROUND}")
        print("\nChapter 1: The Enchanted Forest")
        print(f"{ITALIC}{character_name}, you find yourself in the heart of an enchanted forest, surrounded by towering trees and mystical creatures.")
        print("As you walk deeper into the forest, you encounter a massive tree blocking your path.")
        print("1. Choose to walk around the tree. ")
        print("2. Decide to take on the challenge and try to get rid of the tree. ")

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
        update_character_stats(character_name, health, strength)

        first_chapter_completed = True
        # delay to be able to follow the story better
        time.sleep(2)  # Sleep for 2 seconds

    elif first_chapter_completed and not second_chapter_completed:
            # Display game storyline and choices for Chapter 2
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

                # Update character stats in Google Sheets for Chapter 2
                update_character_stats(character_name, health, strength)
               
            
            second_chapter_completed = True

            # delay to be able to follow the story better
            time.sleep(2)  # Sleep for 2 seconds

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

            # Update character stats in Google Sheets for Chapter 3
            update_character_stats(character_name, health, strength)

                

            third_chapter_completed = True
            # delay to be able to follow the story better
            time.sleep(2)  # Sleep for 2 seconds

        # Display game storyline and choices for Chapter 4
    elif third_chapter_completed and not fourth_chapter_completed:
            # Display game storyline and choices for Chapter 4
            print("\nChapter 4: The Dragon's Lair")
            print("Deep within the castle, you discover a hidden chamber. At the center of the chamber lies a slumbering dragon.")
            print("1. Attempt to sneak past the dragon and continue your quest. ")
            print("2. Wake up the dragon to face it head-on. ")

            # Input validation loop for Chapter 4
            while True:
                choice = input("Enter your choice (1 or 2): ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("To continue your journey you must follow the rules. Choose 1 or 2.")

            if choice == "1":
                print("You silently tiptoe past the dragon, avoiding a fiery confrontation. (+2 Strength)")
                strength += 2
            elif choice == "2":
                print("You awaken the dragon, and a fierce battle ensues. Unfortunately, you were not prepared for this fight and have perished.")
                print("Some heroes have already overreached themselves on the way to glory.")
                print("Unfortunately, you have not been able to earn a place in the Hall of Fame.")
                print("Fortunately, this is a magical adventure. Just try again.")
                 # delay to be able to follow the story better
                time.sleep(4)  # Sleep for 2 seconds
                # Reset all chapter completion variables to start the game again
                first_chapter_completed = False
                second_chapter_completed = False
                third_chapter_completed = False
                fourth_chapter_completed = False
                fifth_chapter_completed = False
                sixth_chapter_completed = False
                seventh_chapter_completed = False
                eighth_chapter_completed = False
                ninth_chapter_completed = False
                tenth_chapter_completed = False
                eleventh_chapter_completed = False
                twelfth_chapter_completed = False
                continue  # Restart the game loop

            # Update character stats in Google Sheets for Chapter 4
            update_character_stats(character_name, health, strength)
            
            fourth_chapter_completed = True
            # delay to be able to follow the story better
            time.sleep(2)  # Sleep for 2 seconds

    elif fourth_chapter_completed and not fifth_chapter_completed:
            # Display game storyline and choices for Chapter 5
            print("\nChapter 5: The Lost Temple")
            print(f"{ITALIC}{character_name}, your journey leads you to a dense jungle, and you stumble upon an ancient temple.")
            print("Legends speak of great treasures hidden within, but the temple is said to be cursed.")
            print("1. Enter the temple in search of treasure. ")
            print("2. Avoid the cursed temple and continue your journey.")

            # Input validation loop for Chapter 5
            while True:
                choice = input("Enter your choice (1 or 2): ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("To continue your journey, choose 1 or 2.")

            if choice == "1":
                print("You decide to brave the curse and enter the temple, but it takes a toll on your health. (-3 Health)")
                health -= 3
            elif choice == "2":
                print("You wisely avoid the cursed temple and continue your journey.")
                health += 1

            # Update character stats in Google Sheets for Chapter 5
            update_character_stats(character_name, health, strength)
            
            fifth_chapter_completed = True

            # Introduce a delay before moving to Chapter 6
            time.sleep(2)  # Sleep for 2 seconds (adjust the delay as needed)

    elif fifth_chapter_completed and not sixth_chapter_completed:
            # Display game storyline and choices for Chapter 6
            print("\nChapter 6: The Desert Oasis")
            print(f"{ITALIC}{character_name}, you find yourself in a vast desert with no end in sight.")
            print("You're thirsty and exhausted when you suddenly spot an oasis in the distance.")
            print("1. Rush towards the oasis in desperation. ")
            print("2. Approach the oasis cautiously. ")

            # Input validation loop for Chapter 6
            while True:
                choice = input("Enter your choice (1 or 2): ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("To continue your journey, choose 1 or 2.")

            if choice == "1":
                print("Your thirst drives you to rush towards the oasis, but it's a mirage! You lose health and gain strength. (-2 Health, +2 Strength)")
                health -= 2
                strength += 2
            elif choice == "2":
                print("You approach the oasis cautiously, preserving your health and feeling refreshed. (+1 Health)")
                health += 1

            # Update character stats in Google Sheets for Chapter 6
            update_character_stats(character_name, health, strength)
            
            sixth_chapter_completed = True

            # Introduce a delay before moving to Chapter 7
            time.sleep(2)  # Sleep for 2 seconds (adjust the delay as needed)

    elif sixth_chapter_completed and not seventh_chapter_completed:
            # Display game storyline and choices for Chapter 7
            print("\nChapter 7: The Enchanted Lake")
            print(f"{ITALIC}{character_name}, your journey leads you to the shores of an enchanted lake.")
            print("You see a magical creature in the water, seemingly beckoning you.")
            print("1. Dive into the lake to meet the creature. ")
            print("2. Stay by the shore and observe from a distance. ")

            # Input validation loop for Chapter 7
            while True:
                choice = input("Enter your choice (1 or 2): ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("To continue your journey, choose 1 or 2.")

            if choice == "1":
                print("You dive into the lake to meet the creature, but it's a test of your courage and health. (-3 Health)")
                health -= 3
            elif choice == "2":
                print("You stay by the shore and observe the creature from a distance, preserving your health.")
                health += 1

            # Update character stats in Google Sheets for Chapter 7
            update_character_stats(character_name, health, strength)
            
            seventh_chapter_completed = True

            # Introduce a delay before moving to Chapter 8
            time.sleep(2)  # Sleep for 2 seconds (adjust the delay as needed)

    elif seventh_chapter_completed and not eighth_chapter_completed:
            # Display game storyline and choices for Chapter 8
            print("\nChapter 8: The Forgotten Realm")
            print(f"{ITALIC}{character_name}, your journey takes an unexpected turn as you stumble upon a portal to a forgotten realm.")
            print("This realm is said to hold ancient secrets and untold mysteries.")
            print("1. Enter the portal and explore the forgotten realm. ")
            print("2. Stay on your current path and continue your quest. ")

            # Input validation loop for Chapter 8
            while True:
                choice = input("Enter your choice (1 or 2): ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("To continue your journey, choose 1 or 2.")

            if choice == "1":
                print("You decide to enter the portal and explore the forgotten realm, but it takes a toll on your health. (-3 Health)")
                health -= 3
            elif choice == "2":
                print("You choose to stay on your current path, focusing on your quest and gaining strength. (+2 Strength)")

            # Update character stats in Google Sheets for Chapter 8
            update_character_stats(character_name, health, strength)
            eighth_chapter_completed = True

            # Introduce a delay before moving to Chapter 9
            time.sleep(2)  # Sleep for 2 seconds

    elif eighth_chapter_completed and not ninth_chapter_completed:
            # Display game storyline and choices for Chapter 9
            print("\nChapter 9: The Dark Enchantment")
            print(f"{ITALIC}{character_name}, as you journey further, you encounter a dark enchantment that threatens the land.")
            print("You must decide how to confront this malevolent force.")
            print("1. Confront the enchantment with your newfound strength. ")
            print("2. Seek the help of a wise elder in the nearby village. ")

            # Input validation loop for Chapter 9
            while True:
                choice = input("Enter your choice (1 or 2): ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("To continue your journey, choose 1 or 2.")

            if choice == "1":
                print("You confront the dark enchantment using your newfound strength, but it takes a toll on your health. (-2 Health)")
                health -= 2
            elif choice == "2":
                print("You seek the help of a wise elder in the nearby village, preserving your health and gaining valuable knowledge. (+1 Health)")
                health += 1

            # Update character stats in Google Sheets for Chapter 9
            update_character_stats(character_name, health, strength)
            
            ninth_chapter_completed = True

            # Introduce a delay before moving to Chapter 10
            time.sleep(2)  # Sleep for 2 seconds (adjust the delay as needed)

    elif ninth_chapter_completed and not tenth_chapter_completed:
            # Display game storyline and choices for Chapter 10
            print("\nChapter 10: The Hidden Treasures")
            print(f"{ITALIC}{character_name}, your quest leads you to an ancient library filled with knowledge and hidden treasures.")
            print("You must decide how to explore this mysterious place.")
            print("1. Search for hidden treasures. ")
            print("2. Study ancient tomes and gain knowledge. ")

            # Input validation loop for Chapter 10
            while True:
                choice = input("Enter your choice (1 or 2): ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("To continue your journey, choose 1 or 2.")

            if choice == "1":
                print("You search for hidden treasures in the library, but it takes a toll on your health. (-2 Health, +2 Strength)")
                health -= 2
                strength += 2
            elif choice == "2":
                print("You choose to study ancient tomes and gain valuable knowledge, improving both your health and strength. (+1 Health, +1 Strength)")
                health += 1
                strength += 1

            # Update character stats in Google Sheets for Chapter 10
            update_character_stats(character_name, health, strength)
            
            tenth_chapter_completed = True

            # Introduce a delay before moving to Chapter 11
            time.sleep(2)  # Sleep for 2 seconds (adjust the delay as needed)

    elif tenth_chapter_completed and not eleventh_chapter_completed:
            # Display game storyline and choices for Chapter 11
            print("\nChapter 11: The Elemental Challenge")
            print(f"{ITALIC}{character_name}, your journey takes you to an elemental realm where you must face elemental challenges.")
            print("You must decide how to confront these powerful forces.")
            print("1. Harness the power of the elements. ")
            print("2. Seek the guidance of elemental guardians. ")

            # Input validation loop for Chapter 11
            while True:
                choice = input("Enter your choice (1 or 2): ")
                if choice in ["1", "2"]:
                    break
                else:
                    print("To continue your journey, choose 1 or 2.")

            if choice == "1":
                print("You harness the power of the elements, gaining incredible strength. (+4 Strength)")
                strength += 4
            elif choice == "2":
                print("You seek the guidance of elemental guardians, receiving their blessings and improving your health. (+3 Health)")

            # Update character stats in Google Sheets for Chapter 11
            update_character_stats(character_name, health, strength)
            
            eleventh_chapter_completed = True

            # Introduce a delay before moving to Chapter 12
            time.sleep(2)  # Sleep for 2 seconds (adjust the delay as needed)

    elif eleventh_chapter_completed and not twelfth_chapter_completed:
            # Display game storyline and choices for Chapter 12 (Final Boss)
            print("\nChapter 12: The Demonic Showdown (Final Boss)")
            print(f"{ITALIC}{character_name}, your epic journey culminates in a dark and foreboding chamber.")
            print("Before you stands a colossal, menacing demon, its eyes ablaze with malevolence, and its towering form wreathed in shadow.")
            print("This is the ultimate test of your strength, courage, and wit.")

            # Check if the conditions are met to engage in the final fight
            if strength >= 10 and (first_chapter_completed and second_chapter_completed and third_chapter_completed and fourth_chapter_completed):
                print("You are well-prepared for this final battle, having made the right decisions and grown stronger throughout your journey.")
                print("1. Engage in a fierce battle with the demon, drawing upon all your might and resolve. (+5 Strength)")
                print("2. Attempt to negotiate with the demon, seeking a way to end the conflict peacefully. (+3 Health)")

                # Input validation loop for Chapter 12 (Final Boss)
                while True:
                    choice = input("Enter your choice (1 or 2): ")
                    if choice in ["1", "2"]:
                        break
                    else:
                        print("To face this formidable foe, choose 1 or 2.")

                if choice == "1":
                    print("You steel yourself for a fierce battle with the colossal demon, your heart filled with determination. (+5 Strength)")
                    strength += 5
                    print("With a mighty clash of titans, you engage in an epic battle against the demon, channeling all your strength and skill.")
                    print("The earth shakes, and the very air trembles with the intensity of your confrontation.")
                    print("In a moment of sheer heroism, you emerge victorious, having vanquished the demon and saved the land.")
                    print("Your name will be forever celebrated in legends.")
                elif choice == "2":
                    print("You attempt to negotiate with the colossal demon, seeking a peaceful resolution.")
                    print("However, the demon is merciless and strikes you down without hesitation.")
                    print("Your journey has come to a tragic end.")
                    print("Some heroes have already overreached themselves on the way to glory.")
                    print("Unfortunately, you have not been able to earn a place in the Hall of Fame.")
                    print("Fortunately, this is a magical adventure. Just try again. ☺")
                    # Reset all chapter completion variables to start the game again
                    first_chapter_completed = False
                    second_chapter_completed = False
                    third_chapter_completed = False
                    fourth_chapter_completed = False
                    fifth_chapter_completed = False
                    sixth_chapter_completed = False
                    seventh_chapter_completed = False
                    eighth_chapter_completed = False
                    ninth_chapter_completed = False
                    tenth_chapter_completed = False
                    eleventh_chapter_completed = False
                    twelfth_chapter_completed = False
                    continue  # Restart the game loop

            else:
                print("You stand before the colossal demon, but you realize that you lack the strength and haven't made the right choices in your journey to face this formidable foe.")
                print("You must acknowledge your limitations and seek a different path to achieve victory.")

            twelfth_chapter_completed = True
            
    # Check if the game is completed (e.g., after Chapter 12)
    if (
        first_chapter_completed and
        second_chapter_completed and
        third_chapter_completed and
        fourth_chapter_completed and
        fifth_chapter_completed and
        sixth_chapter_completed and
        seventh_chapter_completed and
        eighth_chapter_completed and
        ninth_chapter_completed and
        tenth_chapter_completed and
        eleventh_chapter_completed and
        twelfth_chapter_completed
    ):
        all_chapters_completed = True

# Transfer character data to the "Hall of Fame" sheet
transfer_to_hall_of_fame(character_name, character_class, health, strength)

# Display the "Hall of Fame" in the console
HallOfFame = SHEET.worksheet('Hall of Fame')
hall_of_fame_data = HallOfFame.get_all_values()

print("\nHall of Fame:")
for row in hall_of_fame_data:
    print(f"Name: {row[0]}, Class: {row[1]}, Health: {row[2]}, Strength: {row[3]}")
    # Exit the game loop
    break