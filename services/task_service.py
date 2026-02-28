import json
import os
import uuid
from datetime import datetime

DATABASE_PATH = os.path.join("data", "database.json")


def load_database():
    with open(DATABASE_PATH, "r") as file:
        return json.load(file)


def save_database(data):
    with open(DATABASE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def create_task(title, description, owner_email):
    data = load_database()

    new_task = {
        "title": title,
        "description": description,
        "owner": owner_email,
        "id": str(uuid.uuid4()),
        "created_at": str(datetime.now())
    }

    data["tasks"].append(new_task)
    save_database(data)

    return "Task created successfully"