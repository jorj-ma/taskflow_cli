from models.base_model import BaseModel

class Task(BaseModel):

    def __init__(self, title, description, due_date=None, assigned_to=None, status="pending"):
        super().__init__()  # Inherit id, created_at, updated_at from BaseModel
        self._title = title
        self._description = description
        self._due_date = due_date  #YYYY-MM-DD
        self._assigned_to = assigned_to  # Username of the user
        self._status = status  # pending or completed

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Task title cannot be empty.")
        self._title = value
        self.save()

    @property
    def status(self):
        return self._status

    def mark_complete(self):
        # Mark the task as completed.
        self._status = "completed"
        self.save()

    def __str__(self):
        return f"[{self._status.upper()}] {self._title} (Due: {self._due_date}, Assigned to: {self._assigned_to})"

    def to_dict(self): 
        return { 
            "id": self.id, 
            "title": self._title, 
            "description": self._description, 
            "due_date": self._due_date, 
            "assigned_to": self._assigned_to, 
            "status": self._status, 
            "created_at": str(self.created_at), 
            "updated_at": str(self.updated_at), 
            } 
    @staticmethod 
    def from_dict(data): 
        task = Task( 
            title=data["title"], 
            description=data["description"], 
            due_date=data.get("due_date"), 
            assigned_to=data["assigned_to"], 
            status=data.get("status", "pending") 
            ) 
        task._id = data.get("id", task.id) 
        return task
    
    def assign_to(self,user):
        self._assigned_to=user.email
        user.add_task(self)
        self.save()
