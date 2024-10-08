# -*- coding: utf-8 -*-
"""Prodigy_CS_01

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y2SIKyOdXX0vf3ZTG8BUmgrQfYFlRkME
"""

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Normalize shift value
    if mode == 'decrypt':
        shift = -shift

    # Traverse through the given text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Handle uppercase letters
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            # Handle lowercase letters
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Keep non-alphabet characters unchanged

    return result

# Input from the user
text = input("Enter message: ")
shift = int(input("Enter shift value: "))
mode = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ")

# Output the result
if mode.lower() == 'encrypt':
    encrypted_text = caesar_cipher(text, shift, 'encrypt')
    print(f"Encrypted Message: {encrypted_text}")
elif mode.lower() == 'decrypt':
    decrypted_text = caesar_cipher(text, shift, 'decrypt')
    print(f"Decrypted Message: {decrypted_text}")
else:
    print("Invalid mode selected!")