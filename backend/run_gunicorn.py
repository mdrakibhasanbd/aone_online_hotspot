from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()
DEBUG = os.getenv("DEBUG", "False") == "True"
SERVER_PORT = os.getenv("SERVER_PORT", "5008")
app = create_app()

if __name__ == "__main__":
    app.run(debug=DEBUG, port=SERVER_PORT, host='0.0.0.0')
