from models import Task
from utilities.helpers import load_data, save_data

def create_task(title, description, owner_email):
    data = load_data()

    new_task = Task(
        title=title,
        description=description,
        assigned_to=owner_email,
        status='pending'
    )

    task_dict = new_task.to_dict()

    data["tasks"].append(task_dict)
    save_data(data)

    return "Task created successfully"


def delete_task(title, owner_email):
    data = load_data()

    tasks = data["tasks"]

    updated_tasks = [
        task for task in tasks
        if not (task["title"] == title and task["assigned_to"] == owner_email)
    ]

    if len(tasks) == len(updated_tasks):
        return "Task not found or permission denied"

    data["tasks"] = updated_tasks
    save_data(data)

    return "Task deleted"


def get_task_by_user(owner_email):
    data = load_data()

    return [
        Task.from_dict(task)
        for task in data["tasks"]
        if task["assigned_to"] == owner_email
    ]