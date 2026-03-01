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