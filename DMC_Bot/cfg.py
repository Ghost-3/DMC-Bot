import os
from pathlib import Path
from dotenv import load_dotenv


dotenv_path = Path(__file__) / '../.env'
if not dotenv_path.exists():
    print("The .env file doesn't exist.")
    exit(-1)

load_dotenv(dotenv_path)

TOKEN = os.environ.get('TOKEN')

PREFIX = ","
