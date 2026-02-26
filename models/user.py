from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, username, email, password, role="user"):
        super().__init__()  # inherit id,created_at,updated_at
        self._username = username
        self._email = email
        self._password = password
        self._role = role

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
