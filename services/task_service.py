from models import Task,User
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

    #attach task to corresponding user
    for user_dict in data['users']:
        if user_dict['email'] ==owner_email:
            user = User(
                username=user_dict['username'],
                email=user_dict['email'],
                password=user_dict['password'],
                role=user_dict['role']
            )
            new_task.assign_to(user)
            break

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

    #remove task from user's _task list
    for user_dict in data["users"]: 
        if user_dict["email"] == owner_email: 
            user = User( 
                username=user_dict["username"], 
                email=user_dict["email"], 
                password=user_dict["password"], 
                role=user_dict["role"] 
                ) 
            # Find the task object to remove 
            for t in user.tasks: 
                if t.title == title and t._assigned_to == owner_email: 
                    user.remove_task(t) 
                    break 
                break


    return "Task deleted"


def get_task_by_user(owner_email): 
        data = load_data() 
        
        # Find the user 
        for user_dict in data["users"]: 
            if user_dict["email"] == owner_email: 
                user = User( 
                    username=user_dict["username"], 
                    email=user_dict["email"], 
                    password=user_dict["password"], 
                    role=user_dict["role"] 
                ) 
                    
                # Populate user's _tasks from persisted data 
                user._tasks = [ 
                    Task.from_dict(task) 
                    for task in data["tasks"] 
                    if task["assigned_to"] == owner_email 
                ] 
                return user.tasks 
            return [] 