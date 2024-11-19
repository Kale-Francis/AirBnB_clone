
from models.base_model import BaseModel

instance = BaseModel()
print(instance)

instance_dict = instance.to_dict()
new_instance = BaseModel(**instance_dict)
print(new_instance)

