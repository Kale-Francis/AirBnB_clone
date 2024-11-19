class Place:
    def __init__(self, *args, **kwargs):
        self.city_id = kwargs.get('city_id')
        self.user_id = kwargs.get('user_id')
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.number_rooms = kwargs.get('number_rooms')
        self.number_bathrooms = kwargs.get('number_bathrooms')
        self.max_guest = kwargs.get('max_guest')
        self.price_by_night = kwargs.get('price_by_night')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
        self.amenity_ids = kwargs.get('amenity_ids')