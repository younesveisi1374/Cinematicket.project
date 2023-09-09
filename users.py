"""
User Module Documentation

This code defines a module that provides functionality related to UUID generation and user authentication. It imports the `getpass` module and then defines a class called `User`.

The `User` class represents a user in the system and handles user-related operations such as counting users and storing usernames. Here's a breakdown of what each part of the code does:

1. The `class User` block is the definition of the `User` class.

2. Inside the `User` class, there are some class-level attributes: `_user_counter` and `_usernames`. `_user_counter` is used to keep track of the total number of users, while `_usernames` is a set used to store all the usernames.

3. The `__init__` method is the constructor for the `User` class. It takes in the `username`, `password`, and optionally the `number_phone`. Inside the constructor, it assigns the validated `username` to the `username` attribute of the object. It also assigns the validated `password` to the `_password` attribute (note the underscore indicating it is intended to be private). The provided `number_phone` parameter value is assigned to the `number_phone` attribute of the object. Finally, it generates a unique ID for the user by calling the `_generate_user_id()` method defined in the `User` class.

4. The `_generate_user_id(cls)` method is a class method that generates a unique ID as a number. It increments the `_user_counter` class attribute by 1 and returns the updated value as the generated user ID.

5. The `_validate_username(self, username)` method is an instance method that validates the username and checks for duplicates. It checks if the given username already exists in the set of usernames (`User._usernames`). If it does, it raises a `ValueError` with the message "Username is already taken". If the username is not taken, it adds the username to the set of usernames and returns the validated username.

6. The `_validate_password(self, password)` method is an instance method that validates the password and checks for the minimum length. It checks if the length of the password is less than 4 characters. If it is, it raises a `ValueError` with the message "Password must be at least 4 characters long". If the password is valid, it returns the validated password.

7. The `update_info(self, new_username=None, new_number_phone=None)` method allows the user to update their information with an optional new username and/or a new number phone. It takes in two parameters: `new_username` (a string) and `new_number_phone` (a string). If a new username is provided, it updates the `username` attribute with the new value. If a new number phone is provided, it updates the `number_phone` attribute with the new value.

8. The `change_password(self)` method prompts the user to enter their current password and then allows them to change their password. It uses the `getpass` module to securely prompt for passwords. First, it prompts the user to enter their current password. If the entered current password does not match the stored password (`self._password`), it prints an error message ("Error: Incorrect current password") and returns. If the entered current password matches the stored password, it prompts the user to enter a new password and confirms the new password. If the entered new passwords do not match, it prints an error message ("Error: New passwords do not match") and returns. If the entered new passwords match, it updates the stored password with the new password and prints a success message ("Password changed successfully").

The rest of the code is not included in the provided snippet, but you would continue adding your own code below the `class User` block.
"""

import getpass
import datetime


class User:
    """
    Represents a user in the system.

    This class handles user related operations such as counting users and storing usernames.
    """

    _user_counter = 0  # Local variable to calculate user numbers
    _usernames = set()  # Set to store usernames
    card_number_counter = 1

    # Rest of your code goes here...

    def __init__(self, username, password, birthdate, number_phone=None):
        self.username = self._validate_username(
            username
        )  # Assigns the validated username to the 'username' attribute of the object
        self._password = self._validate_password(
            password
        )  # Assigns the validated password to the '_password' attribute (note the underscore indicating it is intended to be private)
        self.number_phone = number_phone  # Assigns the provided 'number_phone' parameter value to the 'number_phone' attribute of the object
        self.birthdate = birthdate
        self.registration_date = datetime.datetime.now()
        self.id = (
            User._generate_user_id()
        )  # Automatically generate a unique ID using the '_generate_user_id()' method defined in the 'User' class
        global card_number_counter
        self.id_card_number = User.card_number_counter
        User.card_number_counter += 1
        self.bank_cards = {}

    @classmethod  # Decorator to indicate that the following method is a class method
    def _generate_user_id(cls):
        """
        Generate a unique ID as a number
        """
        cls._user_counter += 1  # Increment the _user_counter class attribute by 1
        return (
            cls._user_counter
        )  # Return the updated value of _user_counter as the generated user ID

    def _validate_username(self, username):
        """
        Validate the username and check for duplicates.
        """
        if (
            username in User._usernames
        ):  # Check if the given username already exists in the set of usernames
            raise ValueError("Username is already taken.")
        User._usernames.add(username)  # Add the username to the set of usernames
        return username

    def _validate_password(self, password):
        """
        Validate the password and check for minimum length.
        """
        if len(password) < 4:  # Check if the password length is less than 4
            raise ValueError("Password must be at least 4 characters long.")
        return password

    def update_info(self, new_username=None, new_number_phone=None):
        """
        Update the user's information with optional new username and/or new number phone.

        Args:
            new_username (str): New username to replace the existing one. Defaults to `None`.
            new_number_phone (str): New number phone to replace the existing one. Defaults to `None`.
        """
        if new_username:  # Check if a new username is provided
            self.username = (
                new_username  # Update the username attribute with the new value
            )
        if new_number_phone:  # Check if a new number phone is provided
            self.number_phone = (
                new_number_phone  # Update the number_phone attribute with the new value
            )

    def change_password(self):
        """
        Prompts the user to enter their current password and returns it as a string.
        """
        current_password = getpass.getpass(
            "Current password: "
        )  # Prompt the user to enter their current password using getpass module

        if (
            self._password != current_password
        ):  # Check if the entered current password does not match the stored password
            print("Error: Incorrect current password.")
            return

        new_password = getpass.getpass(
            "New password: "
        )  # Prompt the user to enter the new password
        new_password_confirm = getpass.getpass(
            "Confirm new password: "
        )  # Prompt the user to confirm the new password

        if (
            new_password != new_password_confirm
        ):  # Check if the entered new passwords do not match
            print("Error: New passwords do not match.")
            return

        self._password = (
            new_password  # Update the stored password with the new password
        )
        print("Password changed successfully.")

    def add_bank_card(
        self, card_name, card_number, card_expire_date, current_card_balance, card_CVV2
    ):
        card_info = {
            "Card Name": card_name,
            "ard Number": card_number,
            "Expire Date": card_expire_date,
            "Minimum Balance": current_card_balance,
            "CVV2": card_CVV2,
        }
        self.bank_cards[self.id_card_number] = card_info

    class check_info_add_card_bank:
        def check_card_number(self, card_number):
            result = len(card_number) != 16 or not card_number.isdigit()
            return result

        def check_card_expire_date(self, card_expire_date):
            result = (
                len(card_expire_date) != 2
                or len(card_expire_date[0]) != 2
                or len(card_expire_date[1]) != 2
            )
            return result

        def check_current_card_balance(self, current_card_balance):
            min_amount = 500000
            result = int(current_card_balance) < min_amount
            return result

        def check_card_CVV2(self, card_CVV2):
            result = len(str(card_CVV2)) != 4
            return result

        @staticmethod
        def show_bank_cards(found_user, card_CVV2, card_expire_date):
            print("Bank Cards: ")
            if found_user.bank_cards:
                for (
                    id_card_number,
                    card_info,
                ) in found_user.bank_cards.items():
                    print(f"Card ID : {id_card_number}")
                    for key, value in card_info.items():
                        if value == card_CVV2:
                            continue
                        if value == card_expire_date:
                            val = "/".join(card_expire_date)
                            print(f"{key} : {val}")
                        else:
                            print(f"{key} : {value}")
            else:
                print("You have no bank cards.")

        @staticmethod
        def edit_card(found_user, user_choice):
            if found_user.bank_cards:
                for (
                    id_card_number,
                    card_info,
                ) in found_user.bank_cards.items():
                    if id_card_number == user_choice:
                        # update dict
                        card_name = input("Enter name for your card: ")
                        card_number = input("Enter your card number (16 digits): ")
                        if found_user.check_info_add_card_bank().check_card_number(
                            card_number
                        ):
                            print(
                                "Error: Invalid card number. It should be exactly 16 digits."
                            )
                        card_expire_date = input(
                            "Enter the expiration date of your card (YY/MM): "
                        ).split("/")
                        if found_user.check_info_add_card_bank().check_card_expire_date(
                            card_expire_date
                        ):
                            print(
                                "Error: Enter the expiration date in the correct format (YY/MM)."
                            )
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

                        card_info["Card Name"] = card_name
                        card_info["Card Number"] = card_number
                        card_info["Expire Date"] = "/".join(card_expire_date)
                        card_info["Minimum Balance"] = current_card_balance
                        card_info["CVV2"] = card_CVV2

                        print("Updated Card Information: ")
                        print(f"Card ID : {id_card_number}")
                        for key, value in card_info.items():
                            print(f"{key} : {value}")

        def delete_bank_card(found_user, card_id):
            if card_id in found_user.bank_cards:
                del found_user.bank_cards[card_id]
                print("The Bank card been successfully Deleted.")
            else:
                print("Error: Bank card with the specified ID not found.")
