from main.validation import validate_postcode
from main.formatting import format_postcode
from main.postcode_data import PostcodeData

def main():
    print("UK Postcode Validator, Formatter, and Info Fetcher")
    print("--------------------------------------------------\n")

    # Initialize the PostcodeData object
    postcode_data = PostcodeData('data/open_postcode_geo.csv')

    while True:
        user_input = input("Enter a UK postcode (or type 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            print("\nThank you for using the application. Goodbye!")
            break

        if not user_input:
            print("No input detected. Please enter a UK postcode.")
            continue

        try:
            print("\nProcessing your input...")

            # Validate the postcode
            is_valid = validate_postcode(user_input)
            validation_message = "Valid" if is_valid else "Invalid"
            print(f"\nValidation result: {validation_message} postcode")

            # Format and get additional info if valid
            if is_valid:
                formatted = format_postcode(user_input)
                print(f"Formatted postcode: {formatted}")

                # Fetch additional information
                info = postcode_data.get_postcode_info(formatted)
                if info:
                    print(f"Additional Information: {info}")
                else:
                    print("No additional information available for this postcode.")
            else:
                print("Note: Invalid postcodes cannot be formatted or fetched for additional info.")

            print("\n-----------------------------------")

        except ValueError as e:
            # Handle any value errors thrown by your methods
            print(f"Error: {e}")
            print("\n-----------------------------------")

if __name__ == "__main__":
    main()
