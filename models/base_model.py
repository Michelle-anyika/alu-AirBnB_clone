#!/usr/bin/python3
"""
Module for the BaseModel class.
This module defines all common attributes/methods for other classes.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A base class that defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        Attributes:
            id (str): Unique identifier for each instance.
            created_at (datetime): The time the instance was created.
            updated_at (datetime): The time the instance was last updated.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__.
        A key '__class__' is added with the class name of the object.
        created_at and updated_at are converted to ISO format strings.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
