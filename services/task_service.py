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

def delete_task(title, owner_email):
    data = load_database()

    tasks = data["tasks"]

    updated_tasks = [
        task for task in tasks
        if not (task["title"] == title and task["owner"] == owner_email)
    ]

    if len(tasks) == len(updated_tasks):
        return "Task not found or permission denied"

    data["tasks"] = updated_tasks
    save_database(data)

    return "Task deleted"