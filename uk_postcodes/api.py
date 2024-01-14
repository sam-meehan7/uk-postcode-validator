import uvicorn
from fastapi import FastAPI, HTTPException
from main.formatting import format_postcode
from main.validation import validate_postcode
from main.postcode_data import PostcodeData

app = FastAPI()

@app.get("/process/{postcode}")
def process_postcode(postcode: str):
    """
    Endpoint to validate and format a UK postcode.
    """
    try:
        is_valid = validate_postcode(postcode)
        if is_valid:
            formatted_postcode = format_postcode(postcode)
            return {"postcode": postcode, "is_valid": is_valid, "formatted_postcode": formatted_postcode}
        else:
            return {"postcode": postcode, "is_valid": is_valid, "formatted_postcode": None}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/details/{postcode}")
def process_postcode_w_additional_info(postcode: str):
    """
    Endpoint to validate, format, and provide additional info about a UK postcode.
    """
        # Initialize the PostcodeData object
    postcode_data = PostcodeData('data/open_postcode_geo.csv')

    try:
        is_valid = validate_postcode(postcode)
        response = {"postcode": postcode, "is_valid": is_valid}

        if is_valid:
            formatted_postcode = format_postcode(postcode)
            response["formatted_postcode"] = formatted_postcode

            # Fetch additional information from the dataset
            additional_info = postcode_data.get_postcode_info(formatted_postcode)
            if additional_info:
                # Add additional information to the response
                response["additional_info"] = additional_info

        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
