# User Registration and Login System

## Overview
This Python program demonstrates a simple user registration and login system. It allows users to register with a username, password, date of birth, and an optional phone number. Registered users can then log in, view and edit their information, change their password, and manage bank cards.

## Functionality
- **User Registration:** Users can create new accounts by providing a username, password, date of birth (in YYYY-MM-DD format), and an optional phone number.
- **User Login:** Registered users can log in using their credentials (username and password).
- **User Management:** Logged-in users can view and edit their profile information and change their password.
- **Bank Account Management:** Users can add, view, edit, and delete bank cards associated with their account.
- **Security:** Passwords are securely stored using the getpass module, ensuring confidentiality.
- **Data Storage:** User data is stored in a dictionary for easy retrieval and management.

## Usage
- Upon running the program, a user menu is displayed with options to register, log in, or exit.
- Users can follow the on-screen prompts to perform their desired actions.
- The program runs indefinitely until the user chooses to exit.

## Code Structure
- The code is structured with a main() function serving as the entry point.
- Modular design separates user management, bank card operations, and data storage.
- A loop keeps the program running until the user chooses to exit.

## Classes and Modules
- **User Class:** Encapsulates user-related functionalities, including data storage, password management, and bank card operations.
- **getpass Module:** Used for secure password input without displaying the password on the screen.
- **datetime Module:** Used for date and time operations to handle the user's date of birth.

## Menu Options
- Register a New User: Option 1 allows users to create a new account by providing their information.
- User Login: Option 2 enables registered users to log in with their username and password.
- Display User Information: After login, users can view their profile details.
- Edit User Information: Users can edit their username and phone number.
- Change Password: Allows users to update their password securely.
- Bank Account Management: Provides options to add, view, edit, and delete bank cards associated with the user's account.
- Log Out: Allows users to log out and return to the main menu.
- Exit: Option 0 exits the program.

## Error Handling
- The program includes error handling for various scenarios, such as incorrect login credentials, invalid data input, and ensuring the program does not crash when encountering errors.

## Files
- `main.py`: Contains the main program code.
- `users.py`: Defines the User class and related functionality.

## How to Run
1. Clone this repository.
2. Run `main.py` using Python 3: `python main.py`.

## Author
Younes VEisi

## License
This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.
