from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
ASSISTANT_SESSION = os.getenv("ASSISTANT_SESSION")
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
DOWNLOADS_DIR = os.getenv("DOWNLOADS_DIR", "downloads")
ADMINS = list(map(int, os.getenv("ADMINS", "").split(",")))
OWNER_ID = int(os.getenv("OWNER_ID", 0))
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", 0))