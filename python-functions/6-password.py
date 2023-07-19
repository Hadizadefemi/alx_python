#!/usr/bin/python3
def validate_password(password):
    if len(password) < 8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isspace():
            return False
        elif char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
    return has_uppercase and has_lowercase and has_digit

if __name__ == "__main__":
    print(validate_password("Abc1h2a3"))         # True
    print(validate_password("password123"))    # False
    print(validate_password("P@ssw0rd"))       # True
    print(validate_password("short"))          # False
    print(validate_password("With Space"))     # False

