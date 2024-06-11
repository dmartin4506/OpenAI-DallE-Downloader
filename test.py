# test.py

import json
import os
from pathlib import Path
from openai import OpenAI

PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"
DATA_DIR = Path.cwd() / "responses"

# Create the directory if it doesn't exist
DATA_DIR.mkdir(exist_ok=True)

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    # Generate the image with the given prompt
    response = client.images.generate(
        prompt=PROMPT,
        n=1,
        size="256x256",
        response_format="b64_json"
    )
    
    # Extract relevant information from the response
    response_dict = {
        'created': response.created,
        'data': [{'url': img.url, 'b64_json': img.b64_json} for img in response.data]
    }
    
    # Create a file name based on the prompt and response creation time
    file_name = DATA_DIR / f"{PROMPT[:5].replace(' ', '_')}-{response.created}.json"
    
    # Save the response to a JSON file
    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(response_dict, file)
    
    print(f"Response saved to {file_name}")

except Exception as e:
    print(f"An error occurred: {e}")
