import json
import os
import hashlib

DATABASE_PATH = os.path.join("data", "database.json")


def load_database():
    with open(DATABASE_PATH, "r") as file:
        return json.load(file)


def save_database(data):
    with open(DATABASE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(email, password):
    data = load_database()


    for user in data["users"]:
        if user["email"] == email:
            return "User already exists"

    hashed_password = hash_password(password)

    new_user = {
        "email": email,
        "password": hashed_password
    }

    data["users"].append(new_user)
    save_database(data)

    return "Registration successful"

def login_user(email, password):
    data = load_database()

    hashed_password = hash_password(password)

    for user in data["users"]:
        if user["email"] == email and user["password"] == hashed_password:
            return "Login successful"

    return "Invalid credentials"