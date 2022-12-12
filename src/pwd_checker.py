import re

def password_strength(password):
  # Check if password is at least 8 characters long
  if len(password) < 8:
    return False

  # Check if password contains at least one uppercase letter
  if not re.search("[A-Z]", password):
    return False

  # Check if password contains at least one lowercase letter
  if not re.search("[a-z]", password):
    return False

  # Check if password contains at least one digit
  if not re.search("[0-9]", password):
    return False

  # Password is strong
  return True
