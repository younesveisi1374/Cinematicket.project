# User and Bank Card Management System

This Python program, consisting of two main files, `main.py` and `users.py`, serves as a user and bank card management system. The program allows users to register, log in, edit their user information, change their password, and manage their bank cards.

## Overview

## Files
- `main.py`: Contains the main program code.
- `users.py`: Defines the User class and related functionality.


### `main.py`

`main.py` is the user interface of the program. It provides a text-based menu for users to interact with the system. The main functionalities of this file include:

1. **User Registration:** Users can register by providing a username, password, date of birth, and an optional phone number. User inputs are validated, and successful registrations are stored in an SQLite database.

2. **User Login:** Registered users can log in by entering their username and password. Upon successful login, users can access their user information and bank card management options.

3. **User Information:** Users can view and edit their user information, including their username and phone number. Password changes are also supported.

4. **Bank Card Management:** Users can add new bank cards, view existing bank cards, edit bank card information, and delete bank cards. Bank card data includes card name, card number, expiration date, current balance, and CVV2.


### `users.py`

`users.py` contains the database management classes and methods used by `main.py`. The key classes and functionalities are as follows:

1. **`sqlite_connection` Class:** This class manages the SQLite database connection. It includes methods to create database tables for users and bank cards.

2. **`User` Class:** This class inherits from `sqlite_connection` and provides user-related functionalities. These functionalities include user registration, login, retrieval of user data, user information updates, password changes, and bank card management (addition, viewing, editing, and deletion).

### `mydatabase.db`
The `mydatabase.db` file is an SQLite3 database file created and managed by the Python program you provided. SQLite3 is a lightweight and serverless relational database engine that is often used for embedded systems and small-scale applications.

In the context of your program, `mydatabase.db` serves as the backend database for storing user information and bank card data. Here's an overview of its purpose and usage:

**Purpose:**

1. **User Data Storage:** The database stores information about registered users, including their usernames, passwords, birthdates, phone numbers (if provided), and registration dates.

2. **Bank Card Data Storage:** The database also stores data related to bank cards, including card names, card numbers, expiration dates, current card balances, and CVV2 numbers. Each bank card entry is associated with a specific user through a foreign key relationship.

**Usage:**

- When a user registers, their registration data (e.g., username, password, birthdate) is inserted into the "users" table of the database.
- When a user adds a bank card, the card's details are inserted into the "bank_cards" table. Each bank card entry includes the user's ID as a foreign key, linking it to the user who owns the card.
- When a user logs in, the program checks the user's provided username and password against the database entries to authenticate the user.
- When a user views their user information or bank cards, the program retrieves the relevant data from the database.
- When a user edits their user information, changes their password, or updates bank card details, the program updates the corresponding database records.
- When a user deletes a bank card, the program removes the associated record from the "bank_cards" table.

In summary, `mydatabase.db` acts as the persistent storage for user and bank card data, allowing your program to maintain user accounts and manage bank cards across multiple program sessions. It ensures that user data is stored securely and can be accessed and modified as needed by the program's functionalities.
## Usage

To run the program:

1. Execute `main.py`.
2. Choose options from the main menu to register, log in, and manage user information and bank cards.

## Dependencies

The program relies on the `sqlite3` library for database management and the `datetime` library for handling date-related operations.

## Conclusion

This Python program offers a simple yet effective user and bank card management system, storing user data and bank card details securely in an SQLite database. Users can conveniently perform various actions related to their account and bank cards through the provided text-based interface.

## Error Handling
- The program includes error handling for various scenarios, such as incorrect login credentials, invalid data input, and ensuring the program does not crash when encountering errors.



## Author
Younes Veisi