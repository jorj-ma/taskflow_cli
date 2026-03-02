from models import User,Task
from utilities.helpers import load_data, save_data


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


def login_user(username, password):
    data = load_data()

    for user_dict in data["users"]:
        existing_user = User(
            username=user_dict["username"],
            email=user_dict["email"],
            password=user_dict["password"],
            role=user_dict["role"]
        )

        if existing_user.username == username and existing_user.check_password(password):
            # Populate tasks for this user
            existing_user._tasks = [
                Task.from_dict(task)
                for task in data["tasks"]
                if task["assigned_to"] == existing_user.email
            ]

            return existing_user

    return None