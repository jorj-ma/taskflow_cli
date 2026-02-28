import json
import os
import hashlib


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
        return json.load(f)

def save_data(data):
    """Saves the data dictionary back to the file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def hash_password(password):
    """Turns password into a secret code (hash)."""
    return hashlib.sha256(password.encode()).hexdigest()