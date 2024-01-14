import re

def validate_postcode(postcode: str) -> bool:
    """
    Validates a UK postcode.

    Args:
    postcode (str): The postcode to validate.

    Returns:
    bool: True if the postcode is valid, False otherwise.
    """
    # Check if the postcode is a string
    if not isinstance(postcode, str):
        raise ValueError("Postcode must be a string")

    # Remove all non-alphanumeric characters and normalize whitespaces
    cleaned_postcode = re.sub(r'[^A-Za-z0-9]', '', postcode).upper()

    # Regular expression for validating UK postcode
    postcode_regex = r"^[A-Z]{1,2}[0-9R][0-9A-Z]?[0-9][ABD-HJLNP-UW-Z]{2}$"

    return re.match(postcode_regex, cleaned_postcode) is not None