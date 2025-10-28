##🔒 Password Strength Checker

A simple Python program that checks whether a password is strong or weak based on a set of predefined criteria such as length, use of uppercase/lowercase letters, digits, and special characters.

📋 Features

✅ Checks if a password meets minimum length (8 characters)

✅ Ensures presence of both uppercase and lowercase letters

✅ Requires at least one numeric digit (0–9)

✅ Requires at least one special character (e.g., ! @ # $ % ^ & *)

✅ Provides clear feedback on whether the password is strong or weak

🧠 Password Strength Criteria

A strong password must satisfy all of the following:

Minimum Length: At least 8 characters

Uppercase Letters: At least one (A–Z)

Lowercase Letters: At least one (a–z)

Digits: At least one numeric digit (0–9)

Special Characters: At least one symbol (e.g., ! @ # $ % ^ & * ( ) - _ = + { } [ ] ? /)

💻 How to Run the Program
1. Clone or Download the Repository
git clone 
cd password-strength-checker

2. Run the Python Script

Make sure you have Python 3.x installed on your system.

Run the program using:

python password_checker.py

3. Enter Your Password

When prompted:

Enter your password to check strength:


Type any password and press Enter

The program will evaluate your password and show whether it is Strong or Weak

🧩 Example Output

Example 1:

Enter your password to check strength: Deepika@24
Password is strong (meets all criteria).


Example 2:

Enter your password to check strength: deepikas
Password is weak. It must satisfy all of the following:
  • At least 8 characters long
  • Contains both uppercase and lowercase letters
  • Contains at least one digit (0-9)
  • Contains at least one special character (e.g., !, @, #, $, %)

Screenshot of the output: 

![This screenshot shows the output for checking strong and weak password](screenshot/password_strength_output.png)

🧱 Project Structure
password-strength-checker/
│
├── password_checker.py    # Main script
├── README.md              # Documentation

🛠️ Dependencies

This program uses only Python’s built-in re (regular expressions) module — no external packages are required.

⚙️ How It Works

The function check_password_strength(password) performs several checks using regular expressions (re.search).

It verifies:

Length

Presence of uppercase, lowercase, digits, and special characters

Returns True if all conditions are met, otherwise False.

The criteria() function takes user input, evaluates the password, and prints a readable message.



🧑‍💻 Author

Deepika Shastri