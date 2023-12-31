"""
This script implements a basic user management system with features like user registration,
login, user information editing, password change,
bank card management, wallet management, and subscription management.

Functions:
- clear_terminal(): Clears the terminal screen based on the user's operating system.
- main(): Entry point of the program. Initializes a user dictionary
and enters an infinite loop to manage user interactions.

Usage:
1. Run the script to start the user management system.
2. The main function presents a menu with options to register a new user, log in, or exit.
3. After logging in, users can access additional menus
for managing their information, bank cards, wallet, and subscriptions.

Note:
- User data is stored in an SQLite database.
- Bank card information includes card name, card number,
expiration date, current card balance, and CVV2.
- Wallet functionality allows users to recharge their wallet balance
using bank cards and buy subscriptions.
- The script includes basic input validation for user inputs.
"""

import os
import datetime
from users import User,Admin


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
    global current_card_balance_for_wallet_recharge
    myuser = User()
    myadmin = Admin()
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
            role_user = myuser.get_user_role()
            username = input("Please enter a username: ")
            while True:
                password = input("Please enter a password: ")
                if len(password) > 4:
                    break
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
            myuser.register_user(username, password, birthdate, role_user, number_phone)

            # Printing a success message
            clear_terminal()
            print("Registration successful.")

        elif choice == "2":
            # User login
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")

            found_user = None  # Variable for storing the found user
            select_data = myuser.select_data(username, password)

            # Check if the provided username and password match a user in the database
            if select_data:
                found_user = myuser.select_user(username, password)
                clear_terminal()

            if found_user:
                server_role = found_user[0]
                role = myuser.get_server_role(server_role)
                if role[0] == "User":
                    print("\nLogin Successful Dear", found_user[1])
                    while True:
                        print("User Menu:")
                        print("1. Display user information")
                        print("2. Edit user information")
                        print("3. Change password")
                        print("4. BankAccount")
                        print("5. buy Sanses")
                        print("6. Log out")
                        user_choice = input("Please enter the desired number for user: ")

                        if user_choice == "1":
                            # Displaying user information (username and phone number)
                            print("Username: ", found_user[1])
                            print("Birthdate: ", found_user[3])
                            print("Phone Number: ", found_user[4])
                            print("Registration Date: ", found_user[5])
                            print("Your subscription type: ", found_user[6])
                            check_subscription = myuser.check_subscription(found_user[0])
                            print("Days left until the end of the subscription:",check_subscription)
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
                                print("5. Wallet")
                                print("6. Back to User Menu")
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
                                                "Error: Invalid card number"
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
                                                "Error: Right format is: (YY/MM)."
                                            )
                                            continue
                                    while True:
                                        current_card_balance = int(
                                            input(
                                                "Enter the current balance(minimum 500,000 Rials): "
                                            )
                                        )
                                        min_amount = 500000
                                        if current_card_balance > min_amount:
                                            break
                                        else:
                                            print(
                                                "Error: minimum 500,000 Rials"
                                            )
                                            continue
                                    while True:
                                        card_cvv2 = int(
                                            input(
                                                "Conditions:\n\
                                                    1-CVV2 number consists of exactly four digits\n\
                                                    2-CVV2 number must contain only digits (0-9)\n\
                                                        Enter the CVV2 of your card (4 digits): "
                                            )
                                        )
                                        if len(str(card_cvv2)) == 4:
                                            break
                                        else:
                                            print(
                                                "CVV2 number must be exactly four \
                                                    digits and contain only digits (0-9)."
                                            )
                                            continue
                                    # Add the bank card to the user's account
                                    myuser.add_bank_card(
                                        found_user[0],
                                        card_name,
                                        card_number,
                                        "/".join(card_expire_date),
                                        current_card_balance,
                                        card_cvv2,
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
                                        card_id = int(input("Choose your card id: "))
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
                                    clear_terminal()
                                    print("Welcome to Wallet Manager!")
                                    while True:
                                        wallet_balance = myuser.show_wallet_balance()
                                        print("Wallet Balance : ", wallet_balance[0])
                                        print("\n1. Recharge wallet")
                                        print("2. Buy a subscription for an account")
                                        print("3. back to BankAccount's Manager")
                                        wallet_choice = input("Please enter the \
                                            desired number for your wallet: ")
                                        if wallet_choice == "1":
                                            clear_terminal()
                                            print("1. Recharge wallet from bank card")
                                            print(
                                                "2. Recharge wallet from internet. \
                                                    (Please do not select this option because \
                                                        it requires authentication \
                                                            and cannot be used in this code)")
                                            user_choice = input("please enter your choice: ")
                                            if user_choice == "1":
                                                clear_terminal()
                                                bank_cards = myuser.select_bank_card()
                                                for card in bank_cards:
                                                    print("Card Id : ", card[0])
                                                    print("Card Name : ", card[2])
                                                    print("Card Number : ", card[3])
                                                    print("Card Expire Date : ", card[4])
                                                    current_card_balance_for_wallet_recharge=card[5]
                                                    print("Card Balance : ", card[5])
                                                while True:
                                                    card_id_wallet = int(input(
                                                        "Choose your card id: "
                                                        ))
                                                    clear_terminal()
                                                    result = myuser.check_card_id(card_id_wallet)
                                                    if result:
                                                        wallet_balance= myuser.show_wallet_balance()
                                                        print("Wallet Balance: ", wallet_balance[0])
                                                        break
                                                    else:
                                                        print(
                                                            "id for bank card is wrong. \
                                                                please rty again"
                                                        )
                                                        continue
                                                while True:
                                                    print("Your card balance: "
                                                        , current_card_balance_for_wallet_recharge)
                                                    wallet_recharge = input(
                                                        "How much do you want to transfer \
                                                            from the balance of \
                                                                the card to the wallet?")
                                                    if int(wallet_recharge) <= int(
                                                            current_card_balance_for_wallet_recharge
                                                            ):
                                                        new_card_balance = int(
                                                            current_card_balance_for_wallet_recharge) - int(wallet_recharge)
                                                        myuser.update_wallet_balance(wallet_recharge, card_id_wallet,
                                                                                    new_card_balance)
                                                        break
                                                    else:
                                                        print(
                                                            "Please enter an amount less than \
                                                                or equal to your card balance \
                                                                    to charge the wallet!!")
                                                        continue
                                        elif wallet_choice == "2":
                                            clear_terminal()
                                            print("Available subscriptions:\n1. Silver\n2. Golden")
                                            new_subscription = input("Please Choose \
                                                and type your Subscription name for your account: ")
                                            myuser.update_subscription(new_subscription, found_user[0])
                                        elif wallet_choice == "3":
                                            clear_terminal()
                                            break
                                elif bank_choice == "6":
                                    # Go back to the User Menu
                                    break
                                else:
                                    print("Error: Unknown operation.")
                            clear_terminal()
                        elif user_choice == "5":
                            clear_terminal()
                            myadmin.admin_get_all_sanses()
                            sanse_id=input("\nPlease enter id movie for buy: ")
                            buy_movie=myuser.buy_sanse(sanse_id)
                            print(buy_movie)
                        elif user_choice == "6":
                            # Log out the user
                            break
                elif role[0] == "Admin":
                    print("\nLogin Successful Dear", found_user[1])
                    while True:
                        print("Admin Menu:")
                        print("1. Add Sanses")
                        print("2. Delete Sanse")
                        print("3. Show Sanses")
                        print("4. Log out")
                        admin_choice = input("Please enter the desired number for admin: ")
                        if admin_choice == "1":
                            while True:
                                clear_terminal()
                                movie_name = input("Enter movie name: ")
                                release_date = input("Enter release date: ")
                                hall_capacity = int(input("Enter hall capacity: "))
                                age_limit = int(input("Enter age limit: "))
                                myadmin.admin_add_sanse(movie_name, release_date, hall_capacity, age_limit)
                                print("Add Sanses was Successful!")
                                add_more = input("Do you want to Add more sanse? Y/N: ")
                                if add_more.upper() == "Y":
                                    continue
                                elif add_more.upper() == "N":
                                    break
                            clear_terminal()
                        elif admin_choice == "2":
                            while True:
                                sans_id = int(input("Enter sans ID: "))
                                myadmin.admin_delete_sanse(sans_id)
                                print("Delete Sanses was Successful!")
                                delete_more = input("Do you want to Delete more sanse? Y/N: ")
                                if delete_more.upper() == "Y":
                                    continue
                                elif delete_more.upper() == "N":
                                    break
                            clear_terminal()
                        elif admin_choice == "3":
                            clear_terminal()
                            myadmin.admin_get_all_sanses()
                        elif admin_choice == "4":
                            break
        else:
            print("Login Failed!!")


if __name__ == "__main__":
    main()
