# Project configuration file

import os
from dotenv import load_dotenv
from pathlib import Path

#Load enviroment variables
load_dotenv()

#Get Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY is not set")

