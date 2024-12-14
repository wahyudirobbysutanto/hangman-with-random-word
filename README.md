# Hangman with Random Word

#### Video Demo:   [https://youtu.be/Uew98uUUa0c]
 
## Overview
Hangman with Random Word is a Python-based terminal game where players guess a randomly selected word within a limited number of attempts. The game includes customizable features such as difficulty levels and player roles. This project demonstrates the use of Python for file handling, pandas for CSV manipulation, and logical flow implementation.

## Features
- Dynamically generates a CSV file containing words categorized by difficulty levels.
- Offers three player roles: **Human**, **Robot**, and **CowBoy**.
- Supports three difficulty levels: **Easy**, **Medium**, and **Hard**.
- Random word selection from the generated CSV file.
- User-friendly input validation and error handling.
- 5 lives to guess the correct word.

## Getting Started
### Prerequisites
- Python 3.8 or later.
- Required Python libraries: `pandas` (install via `pip install pandas`).
- Required Python libraries: `pytest` (install via `pip install pytest`).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/wahyudirobbysutanto/hangman-with-random-word.git
   cd hangman-with-random-word
   ```
2. Install dependencies:
   ```bash
   pip install pandas
   pip install pytest
   ```

### How to Run
1. Run the main program:
   ```bash
   python project.py
   ```
2. Follow the on-screen prompts:
   - Choose your character (1: Human, 2: Robot, 3: CowBoy).
   - Choose the difficulty level (1: Easy, 2: Medium, 3: Hard).
   - Guess the word within 5 lives!

## Program Flow
1. **Generate CSV File:**
   - Words are defined in `guess_words.py` under variables `easy_words`, `medium_words`, and `hard_words`.
   - These words are saved into a CSV file categorized by difficulty.
2. **Choose Player Role:**
   - Players select their role (Human, Robot, or CowBoy).
   - Invalid inputs prompt an error message.
3. **Set Difficulty Level:**
   - Players choose the game difficulty (Easy, Medium, or Hard).
   - Easy: Case-insensitive alphabet words.
   - Medium: Numeric words.
   - Hard: Case-sensitive alphanumeric words.
   - Invalid inputs prompt an error message.
4. **Start the Game:**
   - A word is randomly selected from the CSV file based on the chosen difficulty.
   - Players guess letters or numbers within 5 lives.

## Function Descriptions
### `main()`
- **Purpose:** The entry point for running the game.
- **Workflow:** Calls all the other functions in sequence to implement the game logic.

### `make_csv()`
- **Purpose:** Generates a CSV file containing categorized words from `guess_words.py`.
- **Input:** None.
- **Output:** Creates a `words.csv` file with columns for difficulty (`Easy`, `Medium`, `Hard`).
- **Library Used:** pandas.

### `get_character_choice()`
- **Purpose:** Validates the player’s character choice.
- **Input:** User input for character selection (1, 2, or 3).
- **Output:** Returns the selected character or an error message for invalid inputs.

### `get_difficulty_choice()`
- **Purpose:** Validates the user’s difficulty level choice.
- **Input:** User input for difficulty level (1, 2, or 3).
- **Output:** Returns the selected difficulty or an error message for invalid inputs.

### `get_word_from_csv()`
- **Purpose:** Reads words from the generated CSV file and converts them to a list based on difficulty.
- **Input:** Difficulty level.
- **Output:** List of words for the selected difficulty level.
- **Library Used:** pandas.

### `get_valid_word()`
- **Purpose:** Selects a random word from the provided word list.
- **Input:** List of words.
- **Output:** A randomly chosen word.

## Example Usage
```bash
Welcome to Hangman!
Select your character:
1. Human
2. Robot
3. CowBoy
> 1

Choose difficulty:
1. Easy
2. Medium
3. Hard
> 2

Guess the word: _ _ _ _ _
> 3
Correct!
```

## File Structure
```
Hangman-with-Random-Word/
├── project.py          # Main script to run the game.
├── guess_words.py      # Contains word variables for CSV creation.
├── visual.py           # Contains character model.
├── test_project.py     # Contains script using pytest for testcase.
├── easy_words.csv      # Auto-generated CSV file with categorized words.
├── medium_words.csv    # Auto-generated CSV file with categorized words.
├── hard_words.csv      # Auto-generated CSV file with categorized words.
└── README.md           # Project documentation.
```

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or suggestions, contact [wahyudirobbysutanto@gmail.com](mailto:wahyudirobbysutanto@gmail.com).

---
Thank you for checking out **Hangman with Random Word**. Have fun guessing!
