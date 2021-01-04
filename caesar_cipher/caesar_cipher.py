
# sometimes "key" is used instead of "shift"
def encrypt(plain, shift):

  encrypted_str = ""

  for char in plain:
    digit = int(char)
    shifted_digit = digit + shift
    encrypted_str += str(shifted_digit)

  return encrypted_str


def decrypt(encoded, shift):
  # "-shift" only works for ints
  return encrypt(encoded, -shift)


def crack():
  pass
