import unittest
from unittest.mock import patch
from io import StringIO
import sys

from main import main

class TestUserRegistrationLogin(unittest.TestCase):
    @patch("builtins.input")
    def test_register_new_user(self, mock_input):
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
        mock_input.side_effect = (value for value in ["1", "testuser2", "password1234", "2000-01-01", "","2", "testuser2", "password1234", "5", "0"])

        sys.stdout = fake_output = StringIO()
        main()
        self.assertIn("Login successful!", fake_output.getvalue())
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
    @patch("builtins.input")
    def test_main_login_failure(self, mock_input):
        mock_input.side_effect = (value for value in ["2", "testuser3", "password111", "5", "0"])

        sys.stdout = fake_output = StringIO()
        main()
        self.assertIn("Login Failed!!", fake_output.getvalue())
        
        # Restore stdout
        sys.stdout = sys.__stdout__
if __name__ == "__main__":
    unittest.main()
