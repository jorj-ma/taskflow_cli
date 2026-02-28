import json
import os
from models import BaseModel

DATA_FILE = "data/database.json"

def initialize_db():
    """Creates the database file and folder if they don't exist."""

    if not os.path.exists("data"):
        os.makedirs("data")
    
    
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({"users": [], "tasks": [], "next_task_id": 1}, f)

def load_data():
    """Reads the file and returns the data."""
    initialize_db()
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        BaseModel.id_counter = data.get("next_task_id", 1)
    return data

def save_data(data):
    """Saves the data dictionary back to the file."""
    data["next_task_id"] = BaseModel.id_counter
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)