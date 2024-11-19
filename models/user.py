from models.base_model import BaseModel
class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = BaseModel.first_name
        self.last_name = BaseModel.last_name
        self.email = BaseModel.email
        self.password = BaseModel.password
    def __str__(self):
        return f"{self.first_name} {self.last_name}"