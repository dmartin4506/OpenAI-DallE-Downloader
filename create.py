# create.py

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"


try:
    response = client.images.generate(prompt=PROMPT,
    n=1,
    size="256x256")
    print(response.data[0].url)
except Exception as e:
    print(f"An error occurred: {e}")
