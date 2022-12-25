import re


class PasswordStrength:

    def password_strength(password):
        # Check if password is at least 8 characters long
        if len(password) < 8:
            print("Password is too short")
            return False

        # Check if password contains at least one uppercase letter
        if not re.search("[A-Z]", password):
            print("Password doesn't have any uppercase letters!")
            return False

        # Check if password contains at least one lowercase letter
        if not re.search("[a-z]", password):
            print("Password doesn't have any lowercase letters!")
            return False

        # Check if password contains at least one digit
        if not re.search("[0-9]", password):
            print("Password doesn't have any digits!")
            return False

        # Password is strong
        print("Password is strong!")
        return True
