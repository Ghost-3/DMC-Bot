import os
from pathlib import Path
from dotenv import load_dotenv
import json


dotenv_path = Path(__file__) / '../.env'
if not dotenv_path.exists():
    print("The .env file doesn't exist.")
load_dotenv(dotenv_path)

TOKEN = os.environ.get('DMC_BOT_TOKEN')
if TOKEN is None:
    print("The TOKEN doesn't exist.")
    exit(-1)

CONFIG = None
config_path = Path(os.environ.get("DMC_CONFIG_PATH"))
if not config_path.exists() or config_path.is_dir():
    print("Wrong config path!")
    exit(-1)

with config_path.open("r", encoding="UTF-8") as file:
    CONFIG = json.load(file)
