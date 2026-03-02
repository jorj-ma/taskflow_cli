from models.base_model import BaseModel
from models.task import Task


class User(BaseModel):
    def __init__(self, username, email, password, role="user"):
        super().__init__()  # inherit id,created_at,updated_at
        self._username = username
        self._email = email
        self._password = password
        self._role = role  # admin or user
        self._tasks7=[]

    @property
    def username(self):
        return self._username  # getter property for the username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Username cannot be empty! Please input username.")
        self._username = value
        self.save()  # updates Timestamp

    @property
    def role(self):
        return self._role  # getter property for the role(user or admin)

    def check_password(self, password):
        return self._password == password  # Password Handling

    def __str__(self):
        return f"User:{self._username} ({self._role})"  # formatted string output

    @property
    def email(self):
        return self._email

    @property
    def tasks(self):
        return self._tasks
    
    @property
    def add_task(self,task):
        if not isinstance(task,Task):
            raise TypeError ('Only Task instances can be added')
        if task._assigned_to != self._email:
            raise ValueError('Task must be assihned to the users email.')
        self._tasks.append(task)
        self.save()

    def remove_task(self, task):
        if task in self._tasks:
            self._tasks.remove(task)
            self.save()