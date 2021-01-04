import re

# sometimes "key" is used instead of "shift"
def encrypt(plain_text, shift):

  # split_text = plain_text.split()
  encrypted_str = ""

  for char in plain_text:
    
    # no alphabetic characters
    if not char.isalpha():
      encrypted_str += char

    #encrypt uppercase
    if (char.isupper()):
      encrypted_str += chr((ord(char) + shift - 65) % 26 + 65)

    #encrypt lowercase
    if (char.islower()):
      encrypted_str += chr((ord(char) + shift - 97) % 26 + 97)

  return encrypted_str


def decrypt(encoded, shift):
  # "-shift" only works for ints
  return encrypt(encoded, -shift)


def crack(encrypted_str):
  pass
