from datetime import datetime


class BaseModel:

    id_counter = 1

    def __init__(self):
        self._id = BaseModel.id_counter  # id for object created
        BaseModel.id_counter += 1  # increment the counter for the next object created

        self._created_at = datetime.now()  # Timestamp for when object is created
        self._updated_at = datetime.now() # Timestamp for when the object was last updated

    @property
    def id(self):
        return self._id  # getter property for the object's id

    @property
    def created_at(self):
        return self._created_at  # getter property for the creation timestamp

    @property
    def updated_at(self):
        return self._updated_at  # getter property for the latest update timestamp

    def save(self):
        self._updated_at = datetime.now()  # updates timestamp for updated_at everytime the object is modified
