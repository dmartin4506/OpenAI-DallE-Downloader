# OpenAI-DallE-Downloader
This repo will generate an image with the Open AI DallE API, Store the JSON Response, The script convert.py will read a JSON file. The script then fetches the Base64-encoded string from the JSON data, decodes it, and saves the resulting image data as a PNG file in a directory. Python will even create that directory for you, if necessary.


Note:

# How to Run this Repo (On Mac)
python3 --version 
Confirm that your Python version is up to date 

python -m venv venv
Create the virtual environment 

source venv/bin/activate 
python3 -m pip install openai

then, within the venv, run this every hour or so to retain the API Key as an Environment Variable 
(venv) $ export OPENAI_API_KEY="<your-key-value-here>"

-----------

python3 test.py
Run the Test.py first

then, copy the output path and update the hardcoded variable in convert.py

Then run the convert.py file, with the JSON_FILE variable defintion value updated according to the output of the Test.py execution. 

python3 convert.py

After running this, your Images directory should be updated to contain the PNG file.

# Done!
