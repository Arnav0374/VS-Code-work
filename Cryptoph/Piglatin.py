import random
import os
import sys
import time

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

text = random.choice(open(get_resource_path("sentence list.txt"), "r").readlines()).strip().lower()

# Pig Latin Converter
# This script converts a given text into Pig Latin.
def to_piglatin(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "way"
    else:
        for i, letter in enumerate(word):
            if letter in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"

print("Welcome to the Pig Latin Challenge!")
time.sleep(1)
print("Can you decipher the Pig Latin text below?")
time.sleep(1)
piglatin_text = ' '.join(to_piglatin(word) for word in text.split())


def main():
    print('\033[91m' + piglatin_text + '\033[0m')
    time.sleep(1)
    user_input = input("Try to decipher this Pig Latin text. You can type 'hint' or 'quit' if you want: ").lower().strip()
    time.sleep(1)
    while True:
        if user_input == 'hint':
            print("Rules for Pig Latin:")
            time.sleep(1)
            print("1. If a word starts with a vowel, add 'way' to the end.")
            time.sleep(1)
            print("2. If a word starts with a consonant, move all consonants up till the first vowel to the end and add 'ay'.")
            time.sleep(1)
            print("3. If a word has no vowels, just add 'ay' to the end.")
            time.sleep(1)
            print("All punctuations directly following a word are included in that word's Pig Latin form.")
            time.sleep(1)
            print("Example: 'hello' becomes 'ellohay', 'apple' becomes 'appleway'.")
            time.sleep(1)
            print("Type 'quit' to see the original text, or continue guessing.")
            time.sleep(1)
            user_input = input("Wanna try again? Type your guess: ").lower().strip()
        elif user_input == 'quit':
            print(f"Oh! Here you go. Maybe this'll help you learn: {text}")
            print("This was the original text, by the way.")
            break
        elif user_input == text:
            print("Congratulations! You deciphered the Pig Latin text correctly!")
            break
        else:
            print("That's not correct. Try again or type 'hint' for help.")
            user_input = input("Type your guess: ").lower().strip()
    if user_input == 'quit':
        print("Better luck next time!")
    print("Thanks for playing the Pig Latin Challenge!")
if __name__ == "__main__":
    main()