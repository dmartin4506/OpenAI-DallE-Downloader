# OpenAI-DallE-Downloader
This repo will generate an image with the Open AI DallE API, Store the JSON Response, The script convert.py will read a JSON file. The script then fetches the Base64-encoded string from the JSON data, decodes it, and saves the resulting image data as a PNG file in a directory. Python will even create that directory for you, if necessary.