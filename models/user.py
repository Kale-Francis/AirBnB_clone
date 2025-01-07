#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel

class User(BaseModel):
    """Represents a user for the application.
    
    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
