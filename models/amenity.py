class Amenity:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')