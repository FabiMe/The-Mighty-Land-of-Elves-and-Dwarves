# The Mighty Land of Elves and Dwarves

![image](https://github.com/FabiMe/The-Mighty-Land-of-Elves-and-Dwarves/assets/136444209/68e9a275-8b67-4503-a736-86cff5de5887)
Welcome to "The Mighty Land of Elves and Dwarves," a text-based adventure game where you embark on an epic journey, make crucial decisions, and shape your character's destiny in a land filled with mystical creatures and challenges.
[Try it yourself](https://elves-and-dwarves-f964c4624ea3.herokuapp.com/)
## User Stories

### Visitor Goals
- As a visitor, I want to be able to play an engaging text-based adventure game.
- I want to choose my character's class and name.
- I want to make choices that affect my character's health, strength, and fate.
- I want to complete all the chapters and earn a place in the game's "Hall of Fame."

### Site Owner Goals
- As the site owner, I want to provide an entertaining and interactive gaming experience.
- I want to engage players with a compelling storyline and meaningful choices.
- I want to encourage players to replay the game and try different paths.

## Goals and Objectives

The main goal of "The Mighty Land of Elves and Dwarves" is to provide an immersive and enjoyable text-based adventure game. The objectives include:
- Creating a captivating narrative with branching storylines.
- Offering meaningful choices that impact the player's character and progress.
- Encouraging replayability by allowing players to explore different paths and outcomes.
- Providing a sense of achievement by reaching the "Hall of Fame" through successful gameplay.

## Target Audience

This game is designed for anyone who enjoys interactive storytelling, decision-making, and fantasy adventures. It appeals to players who appreciate a mix of strategy, role-playing, and exploration in a text-based format.

## Features

- Choose Your Character: Select your character class (Elf or Dwarf) and give them a unique name.
- Multiple Chapters: Navigate through a series of chapters, each with its own storyline and choices.
- Character Development: Make decisions that affect your character's health and strength.
- Final Showdown: Face a formidable demon in the ultimate showdown.
- "Hall of Fame": Earn a place in the game's "Hall of Fame" by successfully completing all chapters.
- Replayability: Explore different paths and outcomes by making different choices.

## Testing

## Manual Testing

Manual testing was performed to ensure the proper functionality of "The Mighty Land of Elves and Dwarves" text-based adventure game. The following test cases cover various scenarios and interactions that players might encounter during their experience with the game.

| Description              | Steps to Reproduce                                    | Expected Outcome                                   | Actual Outcome | Pass/Fail |
|--------------------------|--------------------------------------------------------|-----------------------------------------------------|-----------------|-----------|
| Name Input Validation    | Start a new game and leave the character name field empty. Click "Start Game." | An alert message should appear: "Invalid choice. Please enter 1 for Elf or 2 for Dwarf." | As expected | Pass      |
| Character Selection      | Start a new game, choose a character class (Elf or Dwarf), and provide a character name. Click "Start Game." | The game should begin with the selected character class and name. | As expected | Pass      |
| Storyline Progression    | Play through the game by making various choices at different story branches. | The narrative should progress based on the player's choices, leading to different outcomes. | As expected | Pass      |
| Character Stats          | Monitor character health and strength throughout the game by making choices that affect these stats. | Character stats should change in response to player choices, influencing the gameplay. | As expected | Pass      |
| Final Showdown           | Reach the final showdown with the demon and either win or lose the battle. | Winning the battle should result in a victory message, and losing should lead to a defeat message. | As expected | Pass      |
| "Hall of Fame" Entry     | Successfully complete all chapters of the game.       | The player's name should be displayed in the "Hall of Fame" as an achievement. | As expected | Pass      |
| Replayability           | Start a new game with a different character class and name. Make different choices than in a previous playthrough. | The game should offer a distinct experience with varied outcomes based on different choices. | As expected | Pass      |
| Error Handling          | Introduce errors, such as incorrect user input or unexpected inputs. | The game should handle errors gracefully, providing clear feedback and not crashing. | As expected | Pass      |

### Validator Testing
- Validator testing with https://pep8ci.herokuapp.com/ 
- There are no errors except that lines are too long (only lines in which the story is told). I cannot correct this error for the sake of comprehensibility.

## Bugs

- No known bugs at this time.

## Fixed Bugs

### Indentation Issues

- Resolved various indentation mistakes and code formatting inconsistencies to improve code readability and maintainability.

### Chapter 4 Reset

- Fixed a bug in Chapter 4 that was preventing the game from properly resetting when a player chose to wrong decision.

### Google Sheets Integration

- Addressed issues related to Google Sheets integration for the "Hall of Fame" feature:
  - Corrected a bug where only one row was displayed in the "Hall of Fame" instead of showing all player achievements.
  - Improved error handling and communication with Google Sheets to ensure consistent and accurate data retrieval and storage.

These bug fixes enhance the overall gameplay experience and ensure that the game functions smoothly without unexpected errors.

## Deployment (Heroku.com)

The game can be deployed on [Heroku](https://www.heroku.com/) for online accessibility.
1. Create a Heroku account.
2. Connect github repositorie with Heroku account.
3. Add Config Vars
4. Add Buildpacks
5. Activate Automatic deploys
6. Make the first deploy manual to see if issues occur

## Credits

- Content inspiration and storytelling techniques were adapted from classic choose-your-own-adventure books and popular text-based games.
- Special thanks to the open-source community for their contributions to libraries used in this project.

