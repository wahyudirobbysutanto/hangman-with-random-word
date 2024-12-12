
import sys
import random
from guess_words import easy_words, medium_words, hard_words
from visual import human_visual_dict, robot_visual_dict, cowboy_visual_dict
import string

import pandas as pd

def make_csv(param_name,param_list):
    df = pd.DataFrame(param_list)
    df.to_csv(str(param_name)+'.csv', index=False)

def get_character_choice(param_character):
    while True:
        try:
            param_character = int(param_character)
            if (param_character == 1 or param_character == 2 or param_character == 3):
                return ""
            else:
                return f"\nPlease input only 1 or 2 or 3\n"
        except ValueError:
            return f"\nPlease input only 1 or 2 or 3\n"

def get_difficulty_choice(param_difficult):
    while True:
        try:
            param_difficult = int(param_difficult)
            if (param_difficult == 1 or param_difficult == 2 or param_difficult == 3):
                return ""
            else:
                return f"\nPlease input only 1 or 2 or 3\n"
        except ValueError:
            return f"\nPlease input only 1 or 2 or 3\n"

def get_word_from_csv(param_difficulty):
    csv_name = '';
    if (param_difficulty == 1):
        csv_name = f'easy_words'
    elif (param_difficulty == 2):
        csv_name = f'medium_words'
    elif (param_difficulty == 3):
        csv_name = f'hard_words'

    df = pd.read_csv(csv_name+'.csv', header=None, skiprows=1)
    df_list = df.values.astype(str).tolist()
    return df_list

def get_valid_word(param_words):
    try:
        word = random.choice(param_words)  # randomly chooses something from the list
        while '-' in word or ' ' in word:
            word = random.choice(param_words)
        return word
    except:
        return []

def main():
    lives = 5
    used_letters = set()

    make_csv('easy_words',easy_words)
    make_csv('medium_words',medium_words)
    make_csv('hard_words',hard_words)


    prompt = f'Choose your character for this Hangman!\n'
    prompt += f' 1. Human\n 2. Robot \n 3. Cowboy\n'
    print(f"{prompt}")
    result = ""
    character_input = 0
    result = "check!"
    while result != "":
        character_input = input('Character: ')
        result = get_character_choice(character_input)
        if (result != ""):
            print(f'{result}')
        else:
            character_input = int(character_input)

    if (character_input == 1):
        character_input = human_visual_dict
    elif (character_input == 2):
        character_input = robot_visual_dict
    elif (character_input == 3):
        character_input = cowboy_visual_dict

    prompt = f'Choose your difficulty:\n'
    prompt += f' 1. Easy (only alphabet and Case Insensitive\n'
    prompt += f' 2. Medium (Only numeric)\n'
    prompt += f' 3. Hard (alphanumeric and Case Sensitive\n'
    print(f"{prompt}")

    difficulty_input = 0
    result = "check!"
    while result != "":
        difficulty_input = input('Difficulty: ')
        result = get_difficulty_choice(difficulty_input)
        if (result != ""):
            print(f'{result}')
        else:
            difficulty_input = int(difficulty_input)

    words = get_word_from_csv(difficulty_input)

    for i in range(len(words)):
        words[i][0] = str(words[i][0]).rjust(5, '0')

    word = get_valid_word(words)
    if (word == []):
        sys.exit(1)

    word_letters = [letter for word in word for letter in word]


    while len(word_letters) > 0 and lives > 0:

        print(word[0])
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word[0]]
        print(character_input[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ')

        if (difficulty_input == 1 or difficulty_input == 2):
            user_letter = user_letter.lower()

        if user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')
        elif ((difficulty_input == 3 and user_letter.isalnum()) or
              (difficulty_input == 1 and user_letter.isalpha()) or
              (difficulty_input == 2 and user_letter.isnumeric())):
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters = list(filter((user_letter).__ne__, word_letters))
                print('')
            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')
        else:
            print('\nThat is not a valid letter.')

    if (len(word_letters) == 0 and lives > 0):
        print(f"YOU GUESS THE RIGHT WORD. CONGRATULATION!\nWord:{word[0]}")
    else:
        print(f"NICE TRY. GOOD LUCK FOR YOUR NEXT GUESS\nWord:{word[0]}")

if __name__ == '__main__':
    main()
