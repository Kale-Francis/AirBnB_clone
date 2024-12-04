import uuid
from datetime import datetime
from models.engines.file_storage import FileStorage

class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.storage = FileStorage()

    def created_at(datetime):
        return datetime.now()
    
    def updated_at(datetime):
        return datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self, *args, **kwargs):
        if kwargs in FileStorage():
            kwargs.storage = FileStorage.save()
        else:
            self.storage = FileStorage() 
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            kwargs.save()
        return
    
    def to_dict(self):
        return self.__dict__
    
    formatted_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")


if __name__ == "__main__":
    base = BaseModel()
    print(base)

            
    