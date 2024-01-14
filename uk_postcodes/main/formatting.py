import re
from main.validation import validate_postcode

def format_postcode(postcode: str) -> str:
    """
    Formats a UK postcode into a standard format.

    Args:
    postcode (str): The postcode to format.

    Returns:
    str: The formatted postcode.
    """

    if not isinstance(postcode, str):
        raise ValueError("Postcode must be a string")

    # Remove all non-alphanumeric characters and normalize whitespaces
    cleaned_postcode = re.sub(r'[^A-Za-z0-9]', '', postcode).upper()

    # Ensure that the postcode is valid
    if validate_postcode(cleaned_postcode)==False:
        raise ValueError("Invalid postcode format for formatting")

    # Split postcode into outward and inward parts (inward part is always 3 characters)
    outward = cleaned_postcode[:-3]
    inward = cleaned_postcode[-3:]

    return f"{outward} {inward}"