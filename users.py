"""
This script defines classes and methods for managing user registration, bank card information,
wallet balance, and subscriptions in an SQLite database.

Classes:
- sqlite_connection: Manages SQLite database connections.
- User: Inherits from sqlite_connection and provides user-related functionalities.

Methods:
- sqlite_connection.create_table(): Creates database tables for user registration and bank card data if they don't exist.
- sqlite_connection.wallet(): Creates a table for wallet balance data if it doesn't exist.
- User.register_user(username, password, birthdate, number_phone=None): Registers a new user with the provided information.
- User.select_data(username, password): Selects the username and password from the "users" table.
- User.select_user(username, password): Selects all user data based on the provided username and password.
- User.update_info(new_username, new_number_phone, find_id): Updates user information based on the provided parameters.
- User.change_password(new_password, confirm_password, find_id): Changes the user's password.
- User.add_bank_card(user_id, card_name, card_number, card_expire_date, current_card_balance, card_CVV2): Adds a new bank card entry.
- User.select_bank_card(): Retrieves all bank card entries.
- User.check_card_id(card_id): Checks if a bank card with the given card_id exists.
- User.update_info_bank_cards(card_name, card_number, card_id): Updates bank card information.
- User.delete_bank_card(card_id): Deletes a bank card entry and resets card IDs.
- User.show_wallet_balance(): Retrieves the wallet balance.
- User.update_wallet_balance(wallet_recharge, card_id_wallet, new_card_balance): Updates the wallet balance and bank card balance.
- User.update_subscription(new_Subscription, user_id): Updates the user's subscription and subscription expiration date.
- User.check_subscription(user_id): Checks the user's subscription status and updates it if expired.

Usage:
1. Create an instance of the sqlite_connection class to establish a database connection.
2. Call the create_table method to create necessary database tables.
3. Create an instance of the User class for user-related operations.
4. Use the provided methods to perform various database operations.
"""

import sqlite3
from sqlite3 import Error
from datetime import datetime, timedelta


# Define a class for managing SQLite database connections
class sqlite_connection:
    def __init__(self):
        # Connect to an SQLite database file named "mydatabase.db"
        self.connector = sqlite3.connect("mydatabase.db")
        # Create a cursor object to execute SQL queries
        self.cursor = self.connector.cursor()

    def create_table(self):
        # Create a table for user registration data if it doesn't already exist
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                birthdate DATE,
                number_phone Text,
                registration_date TEXT,
                Subscription TEXT DEFAULT 'Silver',
                subscription_balance TEXT DEFAULT 'You have not purchased any special subscription'
                )
        """
        )
        # Create a table for bank card data if it doesn't already exist
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS bank_cards(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        card_name TEXT NOT NULL,
                        card_number TEXT NOT NULL,
                        card_expire_date TEXT NOT NULL,
                        current_card_balance INTEGER NOT NULL,
                        card_CVV2 INTEGER NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users(id))
            """
        )

        # Commit the changes made to the database
        self.connector.commit()

    def wallet(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Wallet_balance(
            Wallet_balance INTEGER)
            """
        )

        # Check if the table is empty
        self.cursor.execute("SELECT COUNT(*) FROM Wallet_balance")
        count = self.cursor.fetchone()[0]

        if count == 0:
            self.cursor.execute(
                """INSERT INTO Wallet_balance(
                    Wallet_balance
                    ) VALUES (?)""",
                ("0",)  # Pass the value as a tuple
            )

        # Commit the changes made to the database
        self.connector.commit()

class User(sqlite_connection):
    def __init__(self):
        super().__init__()
        self.registration_date = datetime.now()

    def register_user(self, username, password, birthdate, number_phone=None):
        # Insert user registration data into the "users" table
        self.cursor.execute(
            """INSERT INTO users(
                username,password,birthdate,number_phone,registration_date
                ) VALUES (?,?,?,?,?)""",
            (username, password, birthdate, number_phone, self.registration_date),
        )
        # Commit the changes made to the database
        self.connector.commit()

    def select_data(self, username, password):
        # Select the username and password from the "users" table where the given username and password match
        self.cursor.execute(
            "SELECT username, password FROM users WHERE username=? AND password=?",
            (username, password),
        )
        # Fetch a single row (result) from the executed query
        result = self.cursor.fetchone()

        return result

    def select_user(self, username, password):
        # Select all columns (*) from the "users" table where the given username and password match
        self.cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password),
        )
        # Fetch all rows that match the executed query
        rows = self.cursor.fetchall()
        # Iterate through the rows and return the first row found
        for row in rows:
            return row

    def update_info(self, new_username, new_number_phone, find_id):
        # Check if either new_username or new_number_phone is provided
        if new_username or new_number_phone:
            # Update the username and number_phone for the user with find_id
            self.cursor.execute(
                "UPDATE users SET username = ?, number_phone = ? WHERE id = ?",
                (new_username, new_number_phone, find_id),
            )
            # Commit the changes to the database
            self.connector.commit()
        else:
            # If neither new_username nor new_number_phone is provided
            # Retrieve the previous values of username and number_phone for the user with find_id
            self.cursor.execute(
                "SELECT username, number_phone FROM users WHERE id = ?",
                (find_id,),
            )
            previous_values = self.cursor.fetchone()
            if previous_values:
                # If previous values exist
                # Extract the previous username and number_phone
                previous_username, previous_number_phone = previous_values
                # Use the previous values if the corresponding new values are not provided
                new_username = new_username or previous_username
                new_number_phone = new_number_phone or previous_number_phone
                # Update the username and number_phone for the user with find_id using the new values
                self.cursor.execute(
                    "UPDATE users SET username = ?, number_phone = ? WHERE id = ?",
                    (new_username, new_number_phone, find_id),
                )
                # Commit the changes to the database
                self.connector.commit()
            else:
                # If previous values do not exist, print a message indicating that the user does not exist
                print("User does not exist")

    def change_password(self, new_password, confirm_password, find_id):
        # Check if both new_password and confirm_password are provided
        if new_password and confirm_password:
            # Update the password for the user with find_id using the confirm_password
            self.cursor.execute(
                "UPDATE users SET password = ? WHERE id = ?",
                (confirm_password, find_id),
            )
            # Commit the changes to the database
            self.connector.commit()
        else:
            # If either new_password or confirm_password is not provided
            # Retrieve the previous value of password for the user with find_id
            self.cursor.execute(
                "SELECT password FROM users WHERE id = ?",
                (find_id,),
            )
            previous_values = self.cursor.fetchone()
            if previous_values:
                # If previous value exists
                # Use the previous value as the confirm_password
                confirm_password = previous_values
                # Update the password for the user with find_id using the confirm_password
                self.cursor.execute(
                    "UPDATE users SET password = ? WHERE id = ?",
                    (confirm_password, find_id),
                )
                # Commit the changes to the database
                self.connector.commit()

    def add_bank_card(
            self,
            user_id,
            card_name,
            card_number,
            card_expire_date,
            current_card_balance,
            card_CVV2,
    ):
        # Insert a new bank card entry into the bank_cards table with the provided parameters
        self.cursor.execute(
            """INSERT INTO bank_cards(
                user_id,card_name,card_number,card_expire_date,current_card_balance,card_CVV2
                ) VALUES (?,?,?,?,?,?)""",
            (
                user_id,
                card_name,
                card_number,
                card_expire_date,
                current_card_balance,
                card_CVV2,
            ),
        )
        # Commit the changes to the database
        self.connector.commit()

    def select_bank_card(self):
        # Retrieve all rows from the bank_cards table
        self.cursor.execute(
            "SELECT * FROM bank_cards",
            (),
        )
        rows = self.cursor.fetchall()
        # Return the retrieved rows
        return rows

    def check_card_id(self, card_id):
        # Retrieve the card_name and card_number for the bank card with the given card_id from the bank_cards table
        self.cursor.execute(
            "SELECT card_name, card_number FROM bank_cards WHERE id = ?",
            (card_id,),
        )
        result = self.cursor.fetchone()
        if result is not None:
            # If a row is found for the given card_id, return the result
            return result

    def update_info_bank_cards(self, card_name, card_number, card_id):
        # Check if both card_name and card_number are provided
        if card_name and card_number:
            # Update the card_name and card_number for the bank card with the given card_id
            self.cursor.execute(
                "UPDATE bank_cards SET card_name = ?, card_number = ? WHERE id = ?",
                (card_name, card_number, card_id),
            )
        else:
            # If either card_name or card_number is not provided, retrieve the previous values for the bank card with the given card_id
            self.cursor.execute(
                "SELECT card_name, card_number FROM bank_cards WHERE id = ?",
                (card_id,),
            )
            previous_values = self.cursor.fetchone()
            if previous_values is not None:
                previous_card_name = previous_values[0]
                previous_card_number = previous_values[1]
                # Determine the new values for card_name and card_number based on the provided values or the previous values
                new_card_name = card_name or previous_card_name
                new_card_number = card_number or previous_card_number
                # Update the bank card with the new values
                self.cursor.execute(
                    "UPDATE bank_cards SET card_name = ?, card_number = ? WHERE id = ?",
                    (new_card_name, new_card_number, card_id),
                )
                print("Update bank card was successful")
        # Commit the changes to the database
        self.connector.commit()

    def delete_bank_card(self, card_id):
        try:
            # Delete the bank card based on the provided card ID
            self.cursor.execute("DELETE FROM bank_cards WHERE id = ?", (card_id,))
            # Commit the changes to the database
            self.connector.commit()
            print("Bank card successfully deleted.")

            # Reset the IDs in the bank_cards table
            self.cursor.execute("UPDATE bank_cards SET id = id - 1")
            # Commit the changes to the database
            self.connector.commit()

            # Reorder the IDs starting from 1
            self.cursor.execute(
                "UPDATE bank_cards SET id = ROW_NUMBER() OVER (ORDER BY id)"
            )
            # Commit the changes to the database
            self.connector.commit()

            print("Bank card IDs reset.")
        except Error as e:
            print(f"An error occurred: {e}")

    def show_wallet_balance(self):
        self.cursor.execute("SELECT * FROM Wallet_balance")
        rows = self.cursor.fetchone()
        # Return the retrieved rows
        return rows

    def update_wallet_balance(self, wallet_recharge, card_id_wallet,new_card_balance):
        self.cursor.execute("UPDATE Wallet_balance SET Wallet_balance = ?", (wallet_recharge,))
        self.cursor.execute("UPDATE bank_cards SET current_card_balance = ? WHERE id = ?", (new_card_balance, card_id_wallet))
        self.connector.commit()
        print("Recharged wallet balance Successful!")

    def update_subscription(self, new_Subscription, user_id):
        current_date = datetime.now()
        expiration_date = current_date + timedelta(days=30)
        expiration_date_str = expiration_date.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("UPDATE users SET Subscription = ?, subscription_balance = ? WHERE id = ?",
                       (new_Subscription, expiration_date_str, user_id))
        self.connector.commit()
        print("Update Subscription was Successful!")
        
    def check_subscription(self, user_id):
        current_date = datetime.now()
        current_date_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("SELECT Subscription, subscription_balance FROM users WHERE id = ?", (user_id,))
        row = self.cursor.fetchone()
        if row:
            subscription_type, expiration_date_str = row
            expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d %H:%M:%S")
            current_date = datetime.now()
            if current_date <= expiration_date:
                remaining_days = (expiration_date - current_date).days
                return remaining_days
            else:
                self.cursor.execute("UPDATE users SET Subscription = ?, subscription_balance = ? WHERE id = ?",
                               ("Silver", "You have not purchased any special subscription", user_id))
                self.connector.commit()
                return "Your subscription has expired, and it has changed to the Silver subscription."

        self.connector.commit()


if __name__ == "__main__":
    db = sqlite_connection()
    db.create_table()
    #db.wallet()
    # myuser = User()
    # sqlite_connection.select_data()
