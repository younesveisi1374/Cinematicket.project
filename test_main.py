"""
This unit test file tests the functionality of the user registration
and login system implemented in the 'main.py' script.

Tested Functions and Classes:
- main(): Entry point of the program that simulates user interactions for registration and login.
- TestUserRegistrationLogin(unittest.TestCase):
A test case class that contains individual test methods for user registration and login scenarios.

Test Scenarios:
1. `test_register_new_user`: Tests the registration of a new user.
It simulates user input for registration and checks if the registration is successful.

2. `test_main_login_success`: Tests the successful login of an existing user.
It simulates user input for login and validates the login success message.

3. `test_main_login_failure`: Tests the failed login attempt
of a user with incorrect credentials. It simulates user input
for login and validates the login failure message.

Usage:
1. Run this unit test script to verify the correctness
of the user registration and login functionality.
2. The `unittest` module is used to define and run test cases.

Note:
- The `@patch` decorator is used to mock the `input` function
to provide predefined input values during testing.
- The test cases capture the program's output and assert against expected output messages.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import sys

from main import main

class TestUserRegistrationLogin(unittest.TestCase):
    """
    This class contains test cases for user registration and login.
    It is used to verify the correctness of the registration and login functionality.
    """
    @patch("builtins.input")
    def test_register_new_user(self, mock_input):
        """
        This method tests the registration of a new user.
        It uses the 'mock_input' function to simulate user input and validate the registration process.
        
        Parameters:
        - mock_input: A patch object used to simulate user input
        
        Returns:
        - None
        """
        # Set the side_effect as a generator function
        mock_input.side_effect = (value for value in ["1", "testuser", "password123", "1990-01-01", "", "0"])

        # Redirect stdout to StringIO
        sys.stdout = fake_output = StringIO()
        main()

        # Assert the desired output
        self.assertIn("Registration successful.", fake_output.getvalue())
        
        # Restore stdout
        sys.stdout = sys.__stdout__

        # Assert any desired conditions after program closure, if necessary.
    @patch("builtins.input")
    def test_main_login_success(self, mock_input):
        """
        This method tests the login process for a successful login.
        It uses the 'mock_input' function to simulate user input
        and asserts the expected behavior of the login process.
        
        Parameters:
        - mock_input: A patch object used to simulate user input
        
        Returns:
        - None
        """
        mock_input.side_effect = (
            value for value in [
                "1", "testuser2", "password1234", "2000-01-01", "",
                "2", "testuser2", "password1234", "5", "0"
            ]
        )
        sys.stdout = fake_output = StringIO()
        main()
        self.assertIn("Login successful!", fake_output.getvalue())
        # Restore stdout
        sys.stdout = sys.__stdout__
    @patch("builtins.input")
    def test_main_login_failure(self, mock_input):
        """
        Test case for testing the login failure scenario in the main() function.
        """
        mock_input.side_effect = (value for value in ["2", "testuser3", "password111", "5", "0"])
        sys.stdout = fake_output = StringIO()
        main()
        self.assertIn("Login Failed!!", fake_output.getvalue())
        sys.stdout = sys.__stdout__
if __name__ == "__main__":
    unittest.main()
