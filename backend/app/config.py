# config.py
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Flask configuration
SECRET_KEY = os.getenv("SECRET_KEY")