"""
The code provided is a Python script that defines several functions for user registration and login, as well as managing bank accounts. 

At the top of the file, several modules are imported: `getpass`, `datetime`, `sqlite_connection` from a custom module `users`, and `os`.

The first function defined is `clear_terminal()`. This function checks the user's operating system and uses the appropriate command to clear the terminal screen.

Next, the `main()` function is defined. This function serves as the entry point of the program. It initializes a database connection, creates an instance of the `User` class, and sets up a loop to display a menu of options to the user until they choose to exit.

Inside the loop, there are three options:
1. If the user chooses "0", the `exit_flag` variable is set to True, causing the loop to exit.
2. If the user chooses "1", they are prompted to enter their username, password, date of birth, and optional phone number. These details are used to register a new user in the database.
3. If the user chooses "2", they are prompted to enter their username and password. The entered credentials are checked against the database, and if they match, the user is logged in and presented with a submenu of options. These options allow the user to view and edit their information, change their password, and manage their bank account.

Overall, this script provides a simple user registration, login, and bank account management system.
"""
import datetime
from users import User
import os


def clear_terminal():
    """
    Clears the terminal screen based on the user's operating system.

    If the operating system is Windows, the 'cls' command is used to clear the terminal.
    For Mac and Linux, the 'clear' command is used.
    """
    if os.name == "nt":
        # For Windows
        _ = os.system("cls")
    else:
        # For Mac and Linux
        _ = os.system("clear")


def main():
    """
    Entry point of the program.

    This function initializes an empty dictionary to store users and enters
    an infinite loop to continue running the program until interrupted.
    """

    myuser = User()
    exit_flag = False  # Flag variable for controlling loop exit

    while not exit_flag:
        clear_terminal()
        print("\nUser Menu:")
        print("1. Register a new user")
        print("2. User login")
        print("0. Exit")
        choice = input("Please enter the desired number: ")
        clear_terminal()

        if choice == "0":
            exit_flag = True  # Set the flag variable to exit the loop

        elif choice == "1":
            # Registering a new user
            username = input("Please enter a username: ")

            while True:
                password = input("Please enter a password: ")
                if len(password) > 4:
                    break
                else:
                    print("Password must be at least 5 characters long.")
                    continue
            while True:
                birthday_str = input(
                    "Enter your date of birth in the format (YYYY-MM-DD): "
                )
                try:
                    birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d")
                    birthdate: str = birthday.strftime("%Y-%m-%d")
                    break
                except ValueError:
                    print("birthdate input is wrong. please try again!")
                    continue

            number_phone = input("Please enter a phone number (optional): ")

            # Checking if an optional phone number is provided
            if number_phone == "":
                number_phone = None

            # Creating a new user using the database
            myuser.register_user(username, password, birthdate, number_phone)

            # Printing a success message
            clear_terminal()
            print("Registration successful.")

        elif choice == "2":
            # User login
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")

            found_user = None  # Variable for storing the found user
            myuser.select_data(username, password)

            # Check if the provided username and password match a user in the database
            if myuser.select_data(username, password):
                found_user = myuser.select_user(username, password)
                print("Login successful!")
                clear_terminal()

            if found_user:
                while True:
                    print("\nLogin Successful Dear", found_user[1])
                    print("\nUser Menu:")
                    print("1. Display user information")
                    print("2. Edit user information")
                    print("3. Change password")
                    print("4. BankAccount")
                    print("5. Log out")
                    user_choice = input("Please enter the desired number for user: ")

                    if user_choice == "1":
                        # Displaying user information (username and phone number)
                        print("Username:", found_user[1])
                        print("Birthdate:", found_user[3])
                        print("Registration Date:", found_user[4])
                        print("Phone Number:", found_user[5])
                        clear_terminal()

                    elif user_choice == "2":
                        # Editing user information
                        new_username = input(
                            "New username (leave blank to keep current): "
                        )
                        new_number_phone = input(
                            "New phone number (leave blank to keep current): "
                        )
                        find_id = found_user[0]
                        myuser.update_info(new_username, new_number_phone, find_id)
                        print("Information updated successfully.")
                        clear_terminal()

                    elif user_choice == "3":
                        new_password = input("New password: ")
                        confirm_password = input("Confirm new password: ")

                        # Check if the new password and confirmation match
                        if new_password == confirm_password:
                            find_id = found_user[0]
                            myuser.change_password(
                                new_password, confirm_password, find_id
                            )
                            print("Password changed successfully.")
                        else:
                            print("Passwords do not match. Please try again.")
                        clear_terminal()

                    # Present menu options for managing bank accounts
                    elif user_choice == "4":
                        clear_terminal()
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
                                # Add a bank card
                                card_name = input("Enter name for your card: ")
                                # Validate and obtain the card number (16 digits)
                                while True:
                                    card_number = input(
                                        "Enter your card number (16 digits): "
                                    )
                                    if len(card_number) == 16:
                                        break
                                    else:
                                        print(
                                            "Error: Invalid card number. It should be exactly 16 digits."
                                        )
                                    continue
                                # Validate and obtain the card expiration date (YY/MM)
                                while True:
                                    card_expire_date = input(
                                        "Enter the expiration date of your card (YY/MM): "
                                    ).split("/")
                                    if (
                                        len(card_expire_date) == 2
                                        and len(card_expire_date[0]) == 2
                                        and len(card_expire_date[1]) == 2
                                    ):
                                        break
                                    else:
                                        print(
                                            "Error: Enter the expiration date in the correct format (YY/MM)."
                                        )
                                        continue
                                # Validate and obtain the current balance of the card (minimum 500,000 Rials)
                                while True:
                                    current_card_balance = int(
                                        input(
                                            "Enter the current balance of your card in Rials (minimum 500,000 Rials): "
                                        )
                                    )
                                    min_amount = 500000
                                    if current_card_balance > min_amount:
                                        break
                                    else:
                                        print(
                                            "Error: Enter a valid current balance of your card (minimum 500,000 Rials)."
                                        )
                                        continue
                                # Validate and obtain the CVV2 of the card (4 digits)
                                while True:
                                    card_CVV2 = int(
                                        input(
                                            "Conditions:\n 1- CVV2 number on a bank card consists of exactly four digits.\n 2- CVV2 number must contain only digits (0 to 9).\nEnter the CVV2 of your card (4 digits): "
                                        )
                                    )
                                    if len(str(card_CVV2)) == 4:
                                        break
                                    else:
                                        print(
                                            "CVV2 number must be exactly four digits and contain only digits (0-9)."
                                        )
                                        continue
                                # Add the bank card to the user's account
                                myuser.add_bank_card(
                                    found_user[0],
                                    card_name,
                                    card_number,
                                    "/".join(card_expire_date),
                                    current_card_balance,
                                    card_CVV2,
                                )
                                print("Bank card added successfully.")
                                clear_terminal()
                            elif bank_choice == "2":
                                clear_terminal()
                                # Retrieve and display all bank cards associated with the user
                                bank_cards = myuser.select_bank_card()
                                for card in bank_cards:
                                    print("Card Id : ", card[0])
                                    print("Card Name : ", card[2])
                                    print("Card Number : ", card[3])
                                    print("Card Expire Date : ", card[4])
                                    print("Card Minimum Balance : ", card[5])
                                    print()  # Add a line break between each bank card
                            elif bank_choice == "3":
                                while True:
                                    # Prompt the user to enter the card ID they want to edit
                                    card_id = int(input("Choose your card id: "))
                                    # Check if the provided card ID exists in the user's bank cards
                                    result = myuser.check_card_id(card_id)
                                    if result:
                                        card_name = input("New name for your card: ")
                                        card_number = input(
                                            "New card number (16 digits): "
                                        )
                                        myuser.update_info_bank_cards(
                                            card_name, card_number, card_id
                                        )
                                        break
                                    else:
                                        print(
                                            "id for bank card is wrong. please rty again"
                                        )
                                        continue
                                clear_terminal()
                            elif bank_choice == "4":
                                card_id = int(
                                    input("Enter The ID of your bank card to delete: ")
                                )
                                # Delete the specified bank card from the user's account
                                myuser.delete_bank_card(card_id)
                                clear_terminal()
                            elif bank_choice == "5":
                                # Go back to the User Menu
                                break

                            else:
                                print("Error: Unknown operation.")
                        clear_terminal()
                    elif user_choice == "5":
                        # Log out the user
                        break
        else:
            print("Login Failed!!")


if __name__ == "__main__":
    main()
