from models.base_model import BaseModel
class User:
    def __init__(self, *args, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"