from models import User
from utilities.helpers import load_data, save_data
import hashlib


def register_user(username, email, password, role="user"):
    data = load_data()

    for user_dict in data["users"]:
        if user_dict["email"] == email:
            return "User already exists"

    new_user = User(username=username, email=email, password=password, role=role)

    user_dict = {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "password": new_user._password,
        "role": new_user.role
    }

    data["users"].append(user_dict)
    save_data(data)

    return "Registration successful"


def login_user(email, password):
    data = load_data()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    for user in data["users"]:
        if user["email"] == email and user["password"] == hashed_password:
            return "Login successful"

    return "Invalid credentials"