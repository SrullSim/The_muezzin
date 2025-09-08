import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CONFIG_DIR = PROJECT_ROOT / "config"



SETTINGS_FILE_PATH = CONFIG_DIR / "settings.json"
try:
    with open(SETTINGS_FILE_PATH, 'r') as f:
        settings = json.load(f)
except FileNotFoundError:
    settings = {}
    print(f"WARNING: Configuration file not found at {SETTINGS_FILE_PATH}. Using defaults.")

KAFKA_HOST = settings.get("KAFKA_HOST", 'localhost:9092')
ELASTIC_HOST = settings.get("ELASTIC_HOST",  "http://localhost:9200")


LOADER_PUB_TOPIC = settings.get("LOADER_PUB_TOPIC", "muezzine_data")

INDEX_NAME = settings.get("INDEX_NAME", "muezzine_data")
TIMESTAMP = settings.get("TIMESTAMP", 1678886400)

MONGO_HOST = settings.get("MONGO_HOST","mongodb://localhost:27017")
DB_NAME = settings.get("DB_NAME", "podcasts_details")
COLLECTION_NAME = settings.get("COLLECTION_NAME" , "metadata")