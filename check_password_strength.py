import re

def check_password_strength(password: str) -> bool:
   
    # Check minimum length
    if len(password) < 8:
        return False

    # Check for uppercase and lowercase
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False

    # Check for at least one digit
    if not re.search(r"\d", password):
        return False

    # Check for at least one special character.
    # Define a set of special characters (you can extend this set if needed)
    special_chars = r"[!@#$%^&*(),.?\":{}|<>\/\[\]\\\-_=+`~]"  # a reasonable set
    if not re.search(special_chars, password):
        return False

    # If all checks passed:
    return True

def criteria():
    password = input("Enter your password to check strength: ")
    if check_password_strength(password):
        print(" Password is strong (meets all criteria).")
    else:
        print(" Password is weak. It must satisfy all of the following:")
        print("   • At least 8 characters long")
        print("   • Contains both uppercase and lowercase letters")
        print("   • Contains at least one digit (0-9)")
        print("   • Contains at least one special character (e.g., !, @, #, $, %)")
    

if __name__ == "__main__":
    criteria()

