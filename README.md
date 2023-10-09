# User and Bank Card Management System

This Python program, authored by Younes Veisi, is designed as a user and bank card management system. It consists of two main files: `main.py` and `users.py`. Additionally, it includes a unit test file, `test_main.py`, to ensure the correctness of the system's functionality. The system empowers users to register, log in, edit their user information, change their passwords, and effectively manage their bank cards.

## Introduction

In an increasingly digital world, managing personal financial information and user profiles is of utmost importance. This user and bank card management system offer a robust solution to these needs. By providing a user-friendly text-based interface, this program enables users to perform various actions related to their accounts and bank cards securely and efficiently.

## Overview

### Files
- `main.py`: Contains the primary program code.
- `users.py`: Defines the `User` class and essential functionalities.
- `test_main.py`: A unit test file for testing the functionality of `main.py`.
- `mydatabase.db`: SQLite3 database for data storage.

### `main.py`

`main.py` is the user-facing component of the program, presenting a menu-driven interface for interacting with the system. Key features of this file include:

1. **User Registration:** Users can create new accounts by supplying a username, password, date of birth, and an optional phone number. The system validates user inputs and stores successful registrations in an SQLite database.

2. **User Login:** Registered users can log in by providing their username and password. Upon successful login, users gain access to their user information and bank card management options.

3. **User Information:** Users can view and edit their user information, including their username and phone number. Password changes are also supported.

4. **Bank Card Management:** Users can add new bank cards, view existing ones, edit card details, and delete bank cards. Bank card data encompasses card names, card numbers, expiration dates, current balances, and CVV2 codes.

### `users.py`

`users.py` contains classes and methods responsible for managing the underlying database and its interactions. Notable components are:

1. **Database Structure:** The database structure created by `users.py` includes the following tables:

   - `users`: Stores user-related information, including usernames, passwords, birthdates, phone numbers (if provided), and registration dates.
   
   - `bank_cards`: Records bank card data, encompassing card names, card numbers, expiration dates, current card balances, and CVV2 codes. Each bank card entry is associated with a specific user through a foreign key relationship.
   
   - `wallet_balance`: Manages wallet balance data for users, allowing recharging using bank cards and buying subscriptions.
   
   - `subscriptions`: Stores user subscription data, including subscription types and expiration dates.

2. **`sqlite_connection` Class:** This class handles the SQLite database connection. It offers methods for creating database tables related to users and bank cards, as well as tables for wallet balances and subscriptions.

3. **`User` Class:** Inheriting from `sqlite_connection`, this class provides user-specific functionality. These functions include user registration, login, retrieval of user data, user information updates, password changes, and bank card management (addition, viewing, editing, and deletion), as well as wallet balance management and subscription handling.

   - `register_user(username, password, birthdate, number_phone=None)`: Registers a new user with the provided information.
   
   - `select_data(username, password)`: Selects the username and password from the "users" table.
   
   - `select_user(username, password)`: Selects all user data based on the provided username and password.
   
   - `update_info(new_username, new_number_phone, find_id)`: Updates user information based on the provided parameters.
   
   - `change_password(new_password, confirm_password, find_id)`: Changes the user's password.
   
   - `add_bank_card(user_id, card_name, card_number, card_expire_date, current_card_balance, card_CVV2)`: Adds a new bank card entry.
   
   - `select_bank_card()`: Retrieves all bank card entries.
   
   - `check_card_id(card_id)`: Checks if a bank card with the given card_id exists.
   
   - `update_info_bank_cards(card_name, card_number, card_id)`: Updates bank card information.
   
   - `delete_bank_card(card_id)`: Deletes a bank card entry and resets card IDs.
   
   - `show_wallet_balance()`: Retrieves the wallet balance.
   
   - `update_wallet_balance(wallet_recharge, card_id_wallet, new_card_balance)`: Updates the wallet balance and bank card balance.
   
   - `update_subscription(new_Subscription, user_id)`: Updates the user's subscription and subscription expiration date.
   
   - `check_subscription(user_id)`: Checks the user's subscription status and updates it if expired.

### `test_main.py`

`test_main.py` is a unit test file specifically designed to test the functionality of the main program, `main.py`. It plays a crucial role in ensuring that the core features of the program, such as user registration, login, and bank card management, work as expected.

Test Scenarios:
1. `test_register_new_user`: This test scenario focuses on testing the registration of a new user. It simulates user input for registration and checks if the registration process is successful. In other words, it verifies that users can create new accounts with valid information.

2. `test_main_login_success`: This scenario is aimed at testing the successful login of an existing user. It simulates user input for login and validates the login success message. In essence, it ensures that users can access their accounts after providing correct login credentials.

3. `test_main_login_failure`: This scenario addresses the case of a failed login attempt by a user with incorrect credentials. It simulates user input for login with incorrect details and validates the login failure message. This test ensures that the system correctly identifies and handles login failures.

Usage:
1. To utilize `test_main.py`, run this unit test script to verify the correctness of the user registration and login functionality provided by `main.py`.
2. The `unittest` module is used to define and run these test cases. Each test case captures the program's output and asserts against expected output messages.

Note:
- The `@patch` decorator is used to mock the `input` function, allowing predefined input values to be provided during testing.

### `mydatabase.db`

`mydatabase.db` is a critical component of the system, serving as the backend SQLite3 database for storing user and bank card data. Its purpose and usage are as follows:

**Purpose:**

1. **User Data Storage:** The database stores user-related information, including usernames, passwords, birthdates, phone numbers (if provided), and registration dates. This data ensures that user profiles are maintained securely.

2. **Bank Card Data Storage:** `mydatabase.db` also records bank card data. This data includes card names, card numbers, expiration dates, current card balances, and CVV2 codes. Each bank card entry is associated with a specific user through a foreign key relationship, providing a structured way to link bank cards to user accounts.

3. **Wallet Balance Management:** The database facilitates wallet balance management, allowing users to recharge their wallet balance using bank cards. This balance can be used to buy subscriptions, providing users with additional functionality.

4. **Subscription Tracking:** `mydatabase.db` includes a mechanism for tracking user subscriptions, such as subscription types and expiration dates, enabling users to access subscription-based services.

**Usage:**

- During user registration, registration data is inserted into the "users" table of the database.
- When adding a bank card, its details are inserted into the "bank_cards" table, with each entry linked to the respective user through a foreign key.
- User login involves authentication against database entries.
- User information and bank card data are retrieved from the database as needed.
- User actions, such as editing user information, changing passwords, or updating bank card details, result in corresponding database updates.
- Deleting a bank card removes the associated record from the "bank_cards" table.

In essence, `mydatabase.db` ensures secure data storage and accessibility, serving as the backbone of this user and bank card management system. It maintains user information, manages bank card data, tracks wallet balances, and enables subscription management, all while ensuring data integrity and security.


...

## Usage

To run the program:

1. Execute `main.py`.
2. Navigate the main menu to register, log in, and manage user information and bank cards.

## Dependencies

The program relies on two main libraries:
...

## Conclusion

This Python program offers a simple yet robust solution for user and bank card management. It stores user data and bank card details securely in an SQLite database, allowing users to perform a range of actions through a user-friendly text-based interface.

## Error Handling

The program incorporates error handling to address various scenarios, such as incorrect login credentials and invalid data input. These measures ensure the program remains robust and resilient, preventing crashes in the event of errors.

# Author
Younes Veisi
