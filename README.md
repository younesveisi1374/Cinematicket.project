# User and Bank Card Management System

This Python program, authored by Younes Veisi, is designed as a user and bank card management system. It consists of two main files: `main.py` and `users.py`. The system empowers users to register, log in, edit their user information, change their passwords, and effectively manage their bank cards.

## Introduction

In an increasingly digital world, managing personal financial information and user profiles is of utmost importance. This user and bank card management system offers a robust solution to these needs. By providing a user-friendly text-based interface, this program enables users to perform various actions related to their accounts and bank cards securely and efficiently.

## Overview

### Files
- `main.py`: Contains the primary program code.
- `users.py`: Defines the `User` class and essential functionalities.
- `mydatabase.db`: SQLite3 database for data storage.

### `main.py`

`main.py` is the user-facing component of the program, presenting a menu-driven interface for interacting with the system. Key features of this file include:

1. **User Registration:** Users can create new accounts by supplying a username, password, date of birth, and an optional phone number. The system validates user inputs and stores successful registrations in an SQLite database.

2. **User Login:** Registered users can log in by providing their username and password. Upon successful login, users gain access to their user information and bank card management options.

3. **User Information:** Users can view and edit their user information, including their username and phone number. Password changes are also supported.

4. **Bank Card Management:** Users can add new bank cards, view existing ones, edit card details, and delete bank cards. Bank card data encompasses card names, card numbers, expiration dates, current balances, and CVV2 codes.

### `users.py`

`users.py` contains classes and methods responsible for managing the underlying database and its interactions. Notable components are:

1. **`sqlite_connection` Class:** This class handles the SQLite database connection. It offers methods for creating database tables related to users and bank cards.

2. **`User` Class:** Inheriting from `sqlite_connection`, this class provides user-specific functionality. These functions include user registration, login, retrieval of user data, user information updates, password changes, and bank card management (addition, viewing, editing, and deletion).

### `mydatabase.db`

The `mydatabase.db` file serves as the backend SQLite3 database for storing user and bank card data. It plays a vital role in ensuring data persistence and accessibility across multiple program sessions. Key points regarding its purpose and usage are:

**Purpose:**

1. **User Data Storage:** The database stores user-related information such as usernames, passwords, birthdates, phone numbers (if provided), and registration dates.

2. **Bank Card Data Storage:** Bank card data is recorded, encompassing card names, card numbers, expiration dates, current card balances, and CVV2 codes. Each bank card entry is associated with a specific user through a foreign key relationship.

**Usage:**

- During user registration, registration data is inserted into the "users" table of the database.
- When adding a bank card, its details are inserted into the "bank_cards" table, with each entry linked to the respective user through a foreign key.
- User login involves authentication against database entries.
- User information and bank card data are retrieved from the database as needed.
- User actions, such as editing user information, changing passwords, or updating bank card details, result in corresponding database updates.
- Deleting a bank card removes the associated record from the "bank_cards" table.

In essence, `mydatabase.db` ensures secure data storage and accessibility, serving as the backbone of this user and bank card management system.

## Usage

To run the program:

1. Execute `main.py`.
2. Navigate the main menu to register, log in, and manage user information and bank cards.

## Dependencies

The program relies on two main libraries:

- `sqlite3`: Utilized for database management.
- `datetime`: Used for date-related operations.

## Conclusion

This Python program offers a simple yet robust solution for user and bank card management. It stores user data and bank card details securely in an SQLite database, allowing users to perform a range of actions through a user-friendly text-based interface.

## Error Handling

The program incorporates error handling to address various scenarios, such as incorrect login credentials and invalid data input. These measures ensure the program remains robust and resilient, preventing crashes in the event of errors.



# Author
Younes Veisi
