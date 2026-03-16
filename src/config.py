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

# Set project base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Set database path
DB_PATH = BASE_DIR / "database" / "invoices.db"

# Set files working directories
INBOX_DIR = BASE_DIR / "data" / "inbox"
ARCHIVE_DIR = BASE_DIR / "data" / "archive"
ERRORS_DIR = BASE_DIR / "data" / "errors"

# Create needed folders if doesn't exist
for directory in [INBOX_DIR, ARCHIVE_DIR, ERRORS_DIR, DB_PATH.parent]:
    directory.mkdir(parents=True, exist_ok=True)

print(BASE_DIR) #Debug
print(DB_PATH) #Debug
print(INBOX_DIR) #Debug
print(ARCHIVE_DIR) #Debug
print(ERRORS_DIR) #Debug    
