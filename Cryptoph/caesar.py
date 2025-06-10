import random
import os
import time
import sys

def get_resource_path(relative_path):
    # Handles resource paths for both PyInstaller and normal execution
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

sentence_file = get_resource_path("sentence list.txt")
try:
    with open(sentence_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        text = random.choice(lines).lower()
except FileNotFoundError:
    print("Error: 'sentence list.txt' not found. Please make sure the file exists in the correct directory.")
    raise SystemExit(1)


def to_caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)


shift = random.randint(1, 25)
cipher_text = to_caesar_cipher(text, shift).lower().strip()

print("Welcome to the Caesar Cipher Challenge!")
time.sleep(1)
print("Type 'quit' to see the original text, or 'hint1', 'hint2', or 'hint3' for hints.")
time.sleep(1)
print("To help with any confusion, any sentences you see will be properly punctuated.")
time.sleep(1)
print("Your task is to decipher the following Caesar Cipher text:")
time.sleep(1)

time.sleep(1)
print('\033[91m' + cipher_text + '\033[0m')
user_input_cipher = input("Try to decipher this Caesar Cipher text: ").lower().strip()
while True:
    if user_input_cipher == 'quit':
        print(f"Oh! Here you go. Maybe this'll help you learn: {text}")
        time.sleep(1)
        print("This was the original text, by the way.")
        time.sleep(1)
        break
    elif user_input_cipher == 'hint1':
        print('abcdefghijklmnopqrstuvwxyz')
        time.sleep(1)
        user_input_cipher = input("Wanna try again? Type your guess: ").lower().strip()
    elif user_input_cipher == 'hint2':
        print(f"The shift value is {len(str(shift))}-digits long.")
        time.sleep(1)
        user_input_cipher = input("Wanna try again? Type your guess: ").lower().strip()
    elif user_input_cipher == 'hint3':
        print(f"The shift value is {shift}.")
        time.sleep(1)
        user_input_cipher = input("Wanna try again? Type your guess: ").lower().strip()
    elif user_input_cipher == text:
        print("Congratulations! You deciphered the Caesar Cipher text correctly!")
        time.sleep(1)
        break
    else:
        print(f"Sorry, that's not correct. The original text was: {text}")
        time.sleep(1)
        print("Better luck next time!")
        time.sleep(1)
        break
    time.sleep(1)
print("Thanks for playing the Caesar Cipher Challenge!")
time.sleep(1)
print("Goodbye!")