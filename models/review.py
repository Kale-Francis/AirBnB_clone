class Review:
    def __init__(self, *args, **kwargs):
        self.place_id = kwargs.get('place_id')
        self.user_id = kwargs.get('user_id')
        self.text = kwargs.get('text')