import unittest
from main.validation import validate_postcode

class TestValidation(unittest.TestCase):

    def test_validate_postcode_valid(self):
        self.assertTrue(validate_postcode("SW1A 1AA"))
        self.assertTrue(validate_postcode("M1 1AA"))

    def test_validate_postcode_invalid(self):
        self.assertFalse(validate_postcode("1234"))
        self.assertFalse(validate_postcode("InvalidPostcode"))
        self.assertFalse(validate_postcode("SW1A !AA"))

    def test_validate_postcode_non_string(self):
        with self.assertRaises(ValueError):
            validate_postcode(1234)

if __name__ == '__main__':
    unittest.main()
