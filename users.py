"""
This script defines classes and methods for managing user registration, bank card information,
wallet balance, and subscriptions in an SQLite database.

Classes:
- sqlite_connection: Manages SQLite database connections.
- User: Inherits from sqlite_connection and provides user-related functionalities.

Methods:
- sqlite_connection.create_table():
Creates database tables for user registration and bank card data if they don't exist.
- sqlite_connection.wallet():
Creates a table for wallet balance data if it doesn't exist.
- User.register_user(username, password, birthdate, number_phone=None):
Registers a new user with the provided information.
- User.select_data(username, password):
Selects the username and password from the "users" table.
- User.select_user(username, password):
Selects all user data based on the provided username and password.
- User.update_info(new_username, new_number_phone, find_id):
Updates user information based on the provided parameters.
- User.change_password(new_password, confirm_password, find_id):
Changes the user's password.
- User.add_bank_card(user_id, card_name, card_number, card_expire_date,
current_card_balance, card_CVV2): Adds a new bank card entry.
- User.select_bank_card():
Retrieves all bank card entries.
- User.check_card_id(card_id):
Checks if a bank card with the given card_id exists.
- User.update_info_bank_cards(card_name, card_number, card_id):
Updates bank card information.
- User.delete_bank_card(card_id):
Deletes a bank card entry and resets card IDs.
- User.show_wallet_balance():
Retrieves the wallet balance.
- User.update_wallet_balance(wallet_recharge, card_id_wallet, new_card_balance):
Updates the wallet balance and bank card balance.
- User.update_subscription(new_Subscription, user_id):
Updates the user's subscription and subscription expiration date.
- User.check_subscription(user_id):
Checks the user's subscription status and updates it if expired.

Usage:
1. Create an instance of the sqlite_connection class to establish a database connection.
2. Call the create_table method to create necessary database tables.
3. Create an instance of the User class for user-related operations.
4. Use the provided methods to perform various database operations.
"""

import sqlite3
from sqlite3 import Error
from datetime import datetime, timedelta
from enum import Enum
from prettytable import PrettyTable

# Define a class for managing SQLite database connections
class SQLiteConnection:
    """
    This class manages SQLite database connections.
    
    It provides methods to connect to an SQLite database file
    and perform operations such as creating tables.
    """
    def __init__(self):
        # Connect to an SQLite database file named "mydatabase.db"
        self.connector = sqlite3.connect("mydatabase.db")
        # Create a cursor object to execute SQL queries
        self.cursor = self.connector.cursor()
    def add_sanse(self, movie_name, release_date, hall_capacity, age_limit):
        """
        Add a new sanse to the SQLite database.
        
        Parameters:
        - movie_name: The name of the movie.
        - release_date: The release date of the movie.
        - hall_capacity: The capacity of the screening hall.
        - age_limit: The age limit for the movie.
        
        Returns:
        None
        
        This method executes an INSERT query on the 'Sanses' table in the SQLite database,
        adding a new sanse with the provided details.
        """
        query = """
                INSERT INTO Sanses (Movie_Name, Release_date, hall_capacity, age_limit)
                VALUES (?, ?, ?, ?)
                """
        self.cursor.execute(query, (movie_name, release_date, hall_capacity, age_limit))
        self.connector.commit()

    def delete_sanse(self, sans_id):
        """
        Deletes a sans from the Sanses table based on the provided sans_id.

        Args:
            sans_id (int): The id of the sans to be deleted.

        Returns:
            None
        """
        self.cursor.execute("DELETE FROM Sanses WHERE id=?", (sans_id,))
        self.connector.commit()

    def get_all_sanses(self):
        """
        Retrieves all sanses from the Sanses table.

        Returns:
            list: A list of rows representing the sanses.
        """
        self.cursor.execute("SELECT * FROM Sanses")
        rows = self.cursor.fetchall()
        return rows
    def create_table(self):
        """
        Creates a table for user registration data if it doesn't already exist.
        
        Returns:
            None
        """
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
                subscription_balance TEXT DEFAULT 'You have not purchased any special subscription',
                role_user TEXT DEFAULT 'User',
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
        self.cursor.execute(
            """CREATE TABLE  IF NOT EXISTS Sanses(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Movie_Name	TEXT NOT NULL,
                        Release_date	TEXT NOT NULL,
                        hall_capacity	INTEGER NOT NULL,
                        age_limit	INTEGER NOT NULL)
            """
        )

        # Commit the changes made to the database
        self.connector.commit()

    def wallet(self):
        """
        Executes a SQL query to create a table called "Wallet_balance" if it doesn't already exist.
        
        Returns:
            None
        """
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


class UserRole(Enum):
    """
    Enumeration representing different user roles.
    
    Attributes:
        USER (str): User role.
        ADMIN (str): Administrator role.
    """
    USER = "User"
    ADMIN = "Admin"
class User(SQLiteConnection):
    """
    Class representing a user with SQLite connection.
    
    Attributes:
        registration_date (datetime): The date and time of user registration.
        admin_code (str): The admin code associated with the user.
    """
    def __init__(self):
        super().__init__()
        self.registration_date = datetime.now()
        self.admin_code = "7798683"
        self.max_wrong_attempts = 2
        self.wrong_attempts = 0
    def get_user_role(self):
        """
        Prompts the user to choose their role for registration.

        Returns:
            str: The chosen user role ("Admin user" or "Regular user").
        """
        print("What is your role:\n1. Admin user\n2. Regular user")
        get_role=input("Please Choose your role ro registration: ")
        if get_role =="1":
            while self.wrong_attempts < self.max_wrong_attempts:
                code_input = input("Enter the admin code: ")
                if code_input == self.admin_code:
                    user_role = UserRole.ADMIN.value
                    break
                else:
                    print("Wrong code. Please try again.")
                    self.wrong_attempts += 1
            if code_input == "2":
                user_role = UserRole.USER.value
        return user_role
    def get_server_role(self, user_id):
        """
        Retrieves the server role for the specified user from the database.

        Args:
            user_id (int): The ID of the user.

        Returns:
            str: The server role of the specified user.
        """
        self.cursor.execute(
            "SELECT role_user FROM users WHERE id=?",
            (user_id,),  # Include a comma after user_id to make it a tuple
        )
        result = self.cursor.fetchone()
        return result
    def register_user(self, username, password, birthdate, role_user, number_phone=None):
        """
        Registers a new user in the system.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
            birthdate (str): The birthdate of the user (format: YYYY-MM-DD).
            role_user (str): The role of the user.
            number_phone (str, optional): The phone number of the user. Default is None.

        Returns:
            bool: True if the user registration was successful, False otherwise.
        """
        # Insert user registration data into the "users" table
        self.cursor.execute(
            """INSERT INTO users(
                username,password,birthdate,number_phone,registration_date,role_user
                ) VALUES (?,?,?,?,?,?)""",
            (username, password, birthdate, number_phone, self.registration_date, role_user),
        )
        # Commit the changes made to the database
        self.connector.commit()
    def select_data(self, username, password):
        """
        Selects data from the "users" table where the given username and password match.

        Args:
            username (str): The username to be used for selection.
            password (str): The password to be used for selection.

        Returns:
            list: A list of tuples containing the selected data from the "users" table.
        """
        self.cursor.execute(
            "SELECT username, password FROM users WHERE username=? AND password=?",
            (username, password),
        )
        # Fetch a single row (result) from the executed query
        result = self.cursor.fetchone()

        return result

    def select_user(self, username, password):
        """
        Selects all columns from the "users" table where the given username and password match.

        Args:
            username (str): The username to be used for selection.
            password (str): The password to be used for selection.

        Returns:
            tuple: A tuple containing the selected user data from the "users" table.
        """
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
        """
        Updates the information of a user based on their ID.

        Args:
            new_username (str): The new username to be updated.
            new_number_phone (str): The new phone number to be updated.
            find_id (int): The ID of the user to be updated.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
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
                previous_username, previous_number_phone = previous_values
                new_username = new_username or previous_username
                new_number_phone = new_number_phone or previous_number_phone
                self.cursor.execute(
                    "UPDATE users SET username = ?, number_phone = ? WHERE id = ?",
                    (new_username, new_number_phone, find_id),
                )
                self.connector.commit()
            else:
                print("User does not exist")
    def change_password(self, new_password, confirm_password, find_id):
        """
        Changes the password of a user based on their ID.

        Args:
            new_password (str): The new password to be set.
            confirm_password (str): The confirmation of the new password.
            find_id (int): The ID of the user whose password needs to be changed.

        Returns:
            bool: True if the password change was successful, False otherwise.
        """
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
            card_cvv2,
    ):
        """
        Adds a bank card to a user's account.

        Args:
            user_id (int): The ID of the user to whom the bank card is being added.
            card_number (str): The number of the bank card being added.

        Returns:
            bool: True if the bank card was successfully added, False otherwise.
        """
        self.cursor.execute(
            """INSERT INTO bank_cards(
                user_id,card_name,card_number,card_expire_date,current_card_balance,card_cvv2
                ) VALUES (?,?,?,?,?,?)""",
            (
                user_id,
                card_name,
                card_number,
                card_expire_date,
                current_card_balance,
                card_cvv2,
            ),
        )
        # Commit the changes to the database
        self.connector.commit()
    def select_bank_card(self):
        """
        Prompts the user to choose their role for registration.

        Returns:
            str: The chosen user role ("Admin user" or "Regular user").
        """
        # Retrieve all rows from the bank_cards table
        self.cursor.execute(
            "SELECT * FROM bank_cards",
            (),
        )
        rows = self.cursor.fetchall()
        # Return the retrieved rows
        return rows

    def check_card_id(self, card_id):
        """
        Retrieves the card_name and card_number for the bank card 
        with the given card_id from the bank_cards table.

        Args:
            card_id (int): The ID of the bank card to be checked.

        Returns:
            tuple: A tuple containing the card_name and card_number 
                for the bank card with the provided card_id.
        """
        self.cursor.execute(
            "SELECT card_name, card_number FROM bank_cards WHERE id = ?",
            (card_id,),
        )
        result = self.cursor.fetchone()
        if result is not None:
            return result
    def update_info_bank_cards(self, card_name, card_number, card_id):
        """
        Updates the information of a bank card with the provided card_id.

        Args:
            card_name (str): The new name for the bank card.
            card_number (str): The new number for the bank card.
            card_id (int): The ID of the bank card to be updated.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if card_name and card_number:
            self.cursor.execute(
                "UPDATE bank_cards SET card_name = ?, card_number = ? WHERE id = ?",
                (card_name, card_number, card_id),
            )
        else:
            self.cursor.execute(
                "SELECT card_name, card_number FROM bank_cards WHERE id = ?",
                (card_id,),
            )
            previous_values = self.cursor.fetchone()
            if previous_values is not None:
                previous_card_name = previous_values[0]
                previous_card_number = previous_values[1]
                new_card_name = card_name or previous_card_name
                new_card_number = card_number or previous_card_number
                self.cursor.execute(
                    "UPDATE bank_cards SET card_name = ?, card_number = ? WHERE id = ?",
                    (new_card_name, new_card_number, card_id),
                )
                print("Update bank card was successful")
        self.connector.commit()
    def delete_bank_card(self, card_id):
        """
        Prompts the user to choose their role for registration.

        Returns:
            str: The chosen user role ("Admin user" or "Regular user").
        """
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
        """
        Retrieves and prints the current wallet balance from the database.
        """
        self.cursor.execute("SELECT * FROM Wallet_balance")
        rows = self.cursor.fetchone()
        # Return the retrieved rows
        return rows

    def update_wallet_balance(self, wallet_recharge, card_id_wallet,new_card_balance):
        """
        Updates the wallet balance and the current card balance in the database.
        
        Args:
            wallet_recharge (int): The amount to be added to the wallet balance.
            card_id_wallet (int): The ID of the bank card associated with the wallet.
            new_card_balance (int): The updated balance of the bank card.
        """
        wallet_update_query = "UPDATE Wallet_balance SET Wallet_balance = ?"
        card_update_query = "UPDATE bank_cards SET current_card_balance = ? WHERE id = ?"
        self.cursor.execute(wallet_update_query, (wallet_recharge,))
        self.cursor.execute(card_update_query, (new_card_balance, card_id_wallet))
        self.connector.commit()
        print("Recharged wallet balance Successful!")
    def update_subscription(self, new_subscription, user_id):
        """
        Updates the subscription details for a user.
        
        Args:
            new_Subscription (str): The new subscription details.
            user_id (int): The ID of the user whose subscription is being updated.
        """
        current_date = datetime.now()
        expiration_date = current_date + timedelta(days=30)
        expiration_date_str = expiration_date.strftime("%Y-%m-%d %H:%M:%S")
        sql_query = "UPDATE users SET Subscription = ?, subscription_balance = ? WHERE id = ?"
        query_params = (new_subscription, expiration_date_str, user_id)
        self.cursor.execute(sql_query, query_params)
        self.connector.commit()
        print("Update Subscription was Successful!")
    def check_subscription(self, user_id):
        """
        Checks the subscription status for a given user.
        
        Args:
            user_id (int): The ID of the user whose subscription status needs to be checked.
        
        Returns:
            bool: True if the user's subscription is active, False otherwise.
        """
        current_date = datetime.now()
        # current_date_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("SELECT Subscription, subscription_balance FROM users WHERE id = ?",
                            (user_id,))
        row = self.cursor.fetchone()
        if row:
            expiration_date_str = row
            expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d %H:%M:%S")
            current_date = datetime.now()
            if current_date <= expiration_date:
                remaining_days = (expiration_date - current_date).days
                return remaining_days
            else:
                self.cursor.execute(
                    "UPDATE users SET Subscription = ?, subscription_balance = ? WHERE id = ?",
                    ("Silver", "You have not purchased any special subscription", user_id)
                )
                self.connector.commit()
                return "Your subscription has expired,and it has changed to the Silver subscription"
        self.connector.commit()
    def buy_sanse(self, sanse_id):
        """
        Buys a sanse with the given ID.
        
        Args:
            sanse_id (int): The ID of the sanse to be bought.
        
        Returns:
            None
        """
        self.cursor.execute("""
                            SELECT * FROM Sanses WHERE id=?""",(sanse_id,))
        rows = self.cursor.fetchall()
        return rows
    def get_available_sanses(self, user_birthday, user_membership_months):
        """
        Get a list of available sanses based on user's birthday and membership duration.
        
        Args:
            user_birthday (str): The birthday of the user (format: YYYY-MM-DD).
            user_membership_months (int): The duration of the user's membership in months.
        
        Returns:
            list: A list of available sanses that meet the given conditions.
        """
        available_sanses = []
        sanses = []
        today = datetime.date.today()
        for sans in sanses:
            release_date = datetime.datetime.strptime(sans["release_date"], "%Y-%m-%d").date()
            age_limit = sans["age_limit"]
            if release_date <= today and sans["hall_capacity"] > 0 \
                    and age_limit <= user_membership_months:
                if today == user_birthday:
                    sans["hall_capacity"] /= 2
                available_sanses.append(sans)
        return available_sanses
    def reserve_sans(self, user_age, selected_sans):
        """
        Reserve a sans based on user's age and selected sans.
        
        Args:
            user_age (int): The age of the user.
            selected_sans (str): The name or identifier of the selected sans.
        
        Returns:
            None
        """
        sanses= []
        if selected_sans in sanses:
            if selected_sans["hall_capacity"] > 0 and user_age >= selected_sans["age_limit"]:
                selected_sans["hall_capacity"] -= 1
                return True
        return False
class Admin(SQLiteConnection):
    """
    A class representing an admin user.
    
    This class inherits from the `sqlite_connection` class and provides additional functionality
    specific to admin users.
    """
    def __init__(self):
        super().__init__()
        self.role = UserRole.ADMIN

    def admin_add_sanse(self, movie_name, release_date, hall_capacity, age_limit):
        """
        Adds a new sanse for a movie.
        
        Args:
            movie_name (str): The name of the movie.
            release_date (str): The release date of the movie.
            hall_capacity (int): The capacity of the movie hall.
            age_limit (int): The age limit for watching the movie.
        """
        self.add_sanse(movie_name, release_date, hall_capacity, age_limit)

    def admin_delete_sanse(self, sans_id):
        """
        Deletes a sanse identified by the given ID.
        
        Args:
            sans_id (int): The ID of the sanse to be deleted.
        """
        self.delete_sanse(sans_id)

    def admin_get_all_sanses(self):
        """
        Retrieves all the sanses from the system and displays them in a table.
        
        Returns:
            PrettyTable: A table containing the ID, Movie Name, Release Date,
                        Hall Capacity, and Age Limit of all the sanses.
        """
        sanses = self.get_all_sanses()
        table = PrettyTable(["ID", "Movie Name", "Release Date", "Hall Capacity", "Age Limit"])
        separator_row = ["-" * 5, "-" * 20, "-" * 13, "-" * 15, "-" * 9]
        for sans in sanses:
            id_movie = sans[0]
            movie_name = sans[1]
            release_date = sans[2]
            hall_capacity = sans[3]
            age_limit = sans[4]
            table.add_row([id_movie,movie_name, release_date, hall_capacity, age_limit])
            table.add_row(separator_row)
        table.del_row(-1)
        print(table.get_string())




if __name__ == "__main__":
    db = SQLiteConnection()
    db.create_table()
    #db.wallet()
    # myuser = User()
    # sqlite_connection.select_data()
