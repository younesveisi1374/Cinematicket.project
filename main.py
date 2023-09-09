"""
User Registration and Login System Documentation

This Python program demonstrates a simple user registration and login system. It allows users to register with a username, password, date of birth, and an optional phone number. Registered users can then log in, view and edit their information, change their password, and manage bank cards.

Table of Contents:
1. Program Overview
2. Functionality
3. Usage
4. Classes and Modules
5. Menu Options
6. Code Structure
7. Error Handling

1. Program Overview:
   The program offers a user-friendly interface for user registration and login. It securely stores user data and provides menu-driven options for interacting with the system.

2. Functionality:
   - User Registration: Users can create new accounts by providing a username, password, date of birth (in YYYY-MM-DD format), and an optional phone number.
   - User Login: Registered users can log in using their credentials (username and password).
   - User Management: Logged-in users can view and edit their profile information and change their password.
   - Bank Account Management: Users can add, view, edit, and delete bank cards associated with their account.
   - Security: Passwords are securely stored using the getpass module, ensuring confidentiality.
   - Data Storage: User data is stored in a dictionary for easy retrieval and management.

3. Usage:
   - Upon running the program, a user menu is displayed with options to register, log in, or exit.
   - Users can follow the on-screen prompts to perform their desired actions.
   - The program runs indefinitely until the user chooses to exit.

4. Classes and Modules:
   - User Class: Defined in the "users" module, this class encapsulates user-related functionalities, including data storage, password management, and bank card operations.
   - getpass Module: Used for secure password input without displaying the password on the screen.
   - datetime Module: Used for date and time operations to handle the user's date of birth.

5. Menu Options:
   - Register a New User: Option 1 allows users to create a new account by providing their information.
   - User Login: Option 2 enables registered users to log in with their username and password.
   - Display User Information: After login, users can view their profile details.
   - Edit User Information: Users can edit their username and phone number.
   - Change Password: Allows users to update their password securely.
   - Bank Account Management: Provides options to add, view, edit, and delete bank cards associated with the user's account.
   - Log Out: Allows users to log out and return to the main menu.
   - Exit: Option 0 exits the program.

6. Code Structure:
   - The code is structured with a main() function serving as the entry point.
   - Modular design separates user management, bank card operations, and data storage.
   - A loop keeps the program running until the user chooses to exit.

7. Error Handling:
   - The program includes error handling for various scenarios, such as incorrect login credentials, invalid data input, and ensuring the program does not crash when encountering errors.
"""

import getpass
import datetime
from users import User

# Rest of the code...


def main():
    """
    Entry point of the program.

    This function initializes an empty dictionary to store users and enters
    an infinite loop to continue running the program until interrupted.
    """
    users = {}
    exit_flag = False  # Flag variable for controlling loop exit

    while not exit_flag:
        print("\nUser Menu:")
        print("1. Register a new user")
        print("2. User login")
        print("0. Exit")
        choice = input("Please enter the desired number: ")

        if choice == "0":
            exit_flag = True  # Set the flag variable to exit the loop
        elif choice == "1":
            # Registering a new user
            username = input("Please enter a username: ")
            password = getpass.getpass("Please enter a password: ")
            birthday_str = input("Enter your date of birth in the format (YYYY-MM-DD):")
            birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d")
            number_phone = input("Please enter a phone number (optional): ")
            birthdate = birthday.strftime("%Y-%m-%d")

            # Checking if an optional phone number is provided
            if number_phone == "":
                number_phone = None

            # Creating a new instance of the User class with the provided information
            new_user = User(username, password, birthdate, number_phone)

            # Adding the new user to a dictionary of users using their unique ID as the key
            users[new_user.id] = new_user

            # Printing a success message
            print("Registration successful.")
        elif choice == "2":
            # User login
            username = input("Please enter your username: ")
            password = getpass.getpass("Please enter your password: ")

            found_user = None  # Variable for storing the found user

            # Searching for a user with matching username and password
            for user in users.values():
                if user.username == username and user._password == password:
                    found_user = user  # Storing the found user in a variable
                    break

            if found_user:
                while True:
                    print("\nUser Menu:")
                    print("1. Display user information")
                    print("2. Edit user information")
                    print("3. Change password")
                    print("4. BankAccount")
                    print("5. Log out")
                    user_choice = input("Please enter the desired number for user: ")

                    if user_choice == "1":
                        # Displaying user information (username and phone number)
                        print("Username:", found_user.username)
                        print("Birthdate:", found_user.birthdate)
                        print("Registration Date:", found_user.registration_date)
                        print("Phone Number:", found_user.number_phone)
                    elif user_choice == "2":
                        # Editing user information
                        new_username = input(
                            "New username (leave blank to keep current): "
                        )
                        new_number_phone = input(
                            "New phone number (leave blank to keep current): "
                        )
                        found_user.update_info(new_username, new_number_phone)
                        print("Information updated successfully.")
                    elif user_choice == "3":
                        # Changing user password
                        found_user.change_password()
                    elif user_choice == "4":
                        print("Welcome to BankAccount's Manager")
                        while True:
                            print("1. Add a Bank Card")
                            print("2. Show Card's Bank")
                            print("3. Edit Card Bank")
                            print("4. Delete Card Bank")
                            print("5. Back to User Menu")
                            bank_choice = input(
                                "Please enter the desired number for user: "
                            )
                            if bank_choice == "1":
                                card_name = input("Enter name for your card: ")
                                card_number = input(
                                    "Enter your card number (16 digits): "
                                )
                                if found_user.check_info_add_card_bank().check_card_number(
                                    card_number
                                ):
                                    print(
                                        "Error: Invalid card number. It should be exactly 16 digits."
                                    )
                                    continue
                                card_expire_date = input(
                                    "Enter the expiration date of your card (YY/MM): "
                                ).split("/")
                                if found_user.check_info_add_card_bank().check_card_expire_date(
                                    card_expire_date
                                ):
                                    print(
                                        "Error: Enter the expiration date in the correct format (YY/MM)."
                                    )
                                    continue
                                current_card_balance = int(
                                    input(
                                        "Enter the current balance of your card in Rials (minimum 500,000 Rials): "
                                    )
                                )
                                if found_user.check_info_add_card_bank().check_current_card_balance(
                                    current_card_balance
                                ):
                                    print(
                                        "Error: Enter a valid current balance of your card (minimum 500,000 Rials)."
                                    )
                                    continue
                                card_CVV2 = int(
                                    input(
                                        "Conditions:\n 1- CVV2 number on a bank card consists of exactly four digits.\n 2- CVV2 number must contain only digits (0 to 9).\nEnter the CVV2 of your card (4 digits): "
                                    )
                                )
                                if found_user.check_info_add_card_bank().check_card_CVV2(
                                    card_CVV2
                                ):
                                    print(
                                        "CVV2 number must be exactly four digits and contain only digits (0-9)."
                                    )
                                    continue
                                found_user.add_bank_card(
                                    card_name,
                                    card_number,
                                    card_expire_date,
                                    current_card_balance,
                                    card_CVV2,
                                )
                                print("Bank card added successfully.")
                            elif bank_choice == "2":
                                User.check_info_add_card_bank.show_bank_cards(
                                    found_user, card_CVV2, card_expire_date
                                )
                            elif bank_choice == "3":
                                user_choice = int(input("Choose your card id: "))
                                User.check_info_add_card_bank.edit_card(
                                    found_user, user_choice
                                )
                            elif bank_choice == "4":
                                card_id = int(
                                    input("Enter The ID of your bank card to delete: ")
                                )
                                found_user.check_info_add_card_bank.delete_bank_card(
                                    found_user, card_id
                                )
                            elif bank_choice == "5":
                                break
                            else:
                                print("Error: Unknown operation.")
                    elif user_choice == "5":
                        break
                    else:
                        print("Error: Unknown operation.")
            else:
                print("Error: Incorrect username or password.")


if __name__ == "__main__":
    main()
