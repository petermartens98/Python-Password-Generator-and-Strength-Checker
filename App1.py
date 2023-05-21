import random
import string

def check_password_strength(password):
    # Define criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password)

    # Check if the password meets all criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong password"
    else:
        # Get the reasons why the password is weak
        reasons = []
        if not length_criteria: reasons.append("Too short (include 8+ characters)")
        if not uppercase_criteria: reasons.append("No uppercase letters")
        if not lowercase_criteria: reasons.append("No lowercase letters")
        if not digit_criteria: reasons.append("No digits")
        if not special_char_criteria: reasons.append("No special chars")

        return "Weak password \nReasons: {}".format(", ".join(reasons))


def password_generator(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"
    # Generate a random password of the specified length
    password = "".join(random.choice(characters) for _ in range(length))
    # Ensure that the password contains uppercase, lowercase, special characters, and digits
    while not (any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password)):
        password = "".join(random.choice(characters) for _ in range(length))
    return password


print("---Password Strength Checker and Generator---")
while True:
    # Prompt the user to enter a choice
    choice = input("\nEnter Option\n1. Generate a password\n2. Check the strength of a password\n3. Quit\n")

    # Check the user's choice
    if choice == "1":
        # Generate a password
        length = input("Enter the length of the password ('q' to quit): ")
        if length == 'q': break
        length = int(length)
        password = password_generator(length)
        print("Your password is:", password)

    elif choice == "2":
        # Check the strength of a password
        password = input("Enter the password to check ('q' to quit): ")
        if password == 'q': break
        strength = check_password_strength(password)
        print(strength)

    elif choice == "3": break # Quit

    else:
        # Invalid choice
        print("Invalid choice.")
        
