import random

def generate_password(length, charset):
  password = ""
  for i in range(length):
    password += random.choice(charset)
  return password
