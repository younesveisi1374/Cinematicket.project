"""
This code represents a simple user registration and login system. Here is an explanation of the code:

- The code starts by importing the `getpass` module and the `User` class from the "users" module.

- The `main()` function serves as the entry point of the program. It initializes an empty dictionary to store users and enters an infinite loop to keep running the program until interrupted.

- Inside the loop, a menu is displayed to the user with three options: registering a new user, user login, or exiting the program.

- If the user chooses to register a new user:
- The user is prompted for a username, password, and an optional phone number.
- A new instance of the `User` class is created with the provided information.
- The new user is added to the `users` dictionary using their unique ID as the key.
- A success message is printed.

- If the user chooses to log in:
- The user is prompted for their username and password.
- The code iterates over the values of the `users` dictionary, searching for a user with matching credentials.
- If a match is found, the matched user is stored in the `found_user` variable.
- If there is a `found_user`, another menu is displayed for logged-in users with options to display user information, edit user information, change password, or log out.
- Depending on the user's choice, appropriate actions are performed.
- If the user chooses to log out, they are returned to the main menu.
- If the user provides incorrect username or password, an error message is printed.

- The program runs this way until the user chooses to exit (by entering "0" at the main menu).

The code follows a modular approach, separating functionalities into different functions and modules. It uses classes and dictionaries to store and manage user information. The `getpass` module is used to securely input passwords without displaying them on the screen.
"""

import getpass
from users import User

def main():
    """
    Entry point of the program.
    
    This function initializes an empty dictionary to store users and enters
    an infinite loop to continue running the program until interrupted.
    """
    users = {}
    while True:
        print("\nUser Menu:")
        print("1. Register a new user")
        print("2. User login")
        print("0. Exit")
        choice = input("Please enter the desired number: ")

        if choice == "0":
            break
        elif choice == "1":
            # Prompting user for input
            username = input("Please enter a username: ")
            password = getpass.getpass("Please enter a password: ")
            number_phone = input("Please enter a phone number (optional): ")
        
            # Checking if optional phone number is provided
            if number_phone == "":
                number_phone = None
        
            # Creating a new user object
            new_user = User(username, password, number_phone)
        
            # Adding the new user to a dictionary of users
            users[new_user.id] = new_user
        
            # Printing success message
            print("Registration successful.")
        
        elif choice == "2":
            # Prompting user for input
            username = input("Please enter your username: ")
            password = getpass.getpass("Please enter your password: ")
            
            # Initializing a variable to store the found user
            found_user = None
        
            
            # Searching for the user with matching username and password in the dictionary
            # Iterating over the values of the `users` dictionary
            for user in users.values():
                # Checking if the username and password match
                if user.username == username and user._password == password:
                    # Assigning the matched user to the `found_user` variable
                    found_user = user
                    # Exiting the loop since a matching user has been found
                    break
            

            if found_user:
                while True:
                    print("\nUser Menu:")
                    print("1. Display user information")
                    print("2. Edit user information")
                    print("3. Change password")
                    print("4. Log out")
                    user_choice = input("Please enter the desired number for user: ")

                    if user_choice == "1":
                        # Displaying user information (username and phone number)
                        print(found_user.username, found_user.number_phone)
                    elif user_choice == "2":
                        # Editing user information
                        new_username = input("New username (leave blank to keep current): ")
                        new_number_phone = input("New phone number (leave blank to keep current): ")
                        found_user.update_info(new_username, new_number_phone)
                        print("Information updated successfully.")
                    elif user_choice == "3":
                        # Changing user password
                        found_user.change_password()
                    elif user_choice == "4":
                        # Logging out of the user account
                        break
                    else:
                        print("Error: Unknown operation.")

            else:
                print("Error: Incorrect username or password.")


if __name__ == "__main__":
    main()
