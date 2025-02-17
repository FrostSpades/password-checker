"""
Checks password for strength.

@author Ethan Andrews
@version 2025.2.17
"""

def check_password(password):
    """
    Checks the given password for weaknesses. Returns a list of weaknesses. Returns empty list if password is strong.
    :param password: the password to be checked
    :return: list of weaknesses
    """
    weaknesses = []

    if len(password) < 8:
        weaknesses.append("Password must be at least 8 characters long")

    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        weaknesses.append("Password must contain at least one uppercase letter.")

    # Check for lowercase letters
    if not any(char.islower() for char in password):
        weaknesses.append("Password must contain at least one lowercase letter.")

    # Check for numbers
    if not any(char.isdigit() for char in password):
        weaknesses.append("Password must contain at least one number.")

    # Check for special characters
    special_characters = "!@#$%^&*()-_+=<>?/"
    if not any(char in special_characters for char in password):
        weaknesses.append("Password must contain at least one special character (e.g., !@#$%^&*).")

    # Check for common patterns (e.g., all characters are the same or repeated patterns)
    if password.lower() in ['password', '123456', 'qwerty', 'letmein']:
        weaknesses.append("Password is too common and easily guessable.")

    return weaknesses


if __name__ == '__main__':
    user_password = input("Enter your password: ")
    user_password_weaknesses = check_password(user_password)

    if len(user_password_weaknesses) == 0:
        print("Password is strong")
    else:
        print(user_password_weaknesses)