import unittest
from main.formatting import format_postcode

class TestFormatPostcode(unittest.TestCase):

    def test_format_postcode_valid(self):
        # Test with standard and diverse valid postcodes
        self.assertEqual(format_postcode("sw1a1aa"), "SW1A 1AA")
        self.assertEqual(format_postcode("m11aa"), "M1 1AA")
        self.assertEqual(format_postcode("EC1A 1BB"), "EC1A 1BB")

    def test_format_postcode_invalid(self):
        # Test with an invalid postcode
        with self.assertRaises(ValueError):
            format_postcode("E!!YUP")

    def test_format_postcode_empty_string(self):
        # Test with an empty string
        with self.assertRaises(ValueError):
            format_postcode("")

    def test_format_postcode_whitespace(self):
        # Test with only whitespaces
        with self.assertRaises(ValueError):
            format_postcode("   ")

    def test_format_postcode_non_string(self):
        # Test with non-string input
        with self.assertRaises(ValueError):
            format_postcode(1234)

    def test_format_postcode_short(self):
        # Test with a too-short postcode
        with self.assertRaises(ValueError):
            format_postcode("A1")

    def test_format_postcode_with_special_characters(self):
        # Test with postcodes containing special characters
        self.assertEqual(format_postcode("SW1A-1AA"), "SW1A 1AA")
        self.assertEqual(format_postcode("EC1A@1BB"), "EC1A 1BB")

if __name__ == '__main__':
    unittest.main()
