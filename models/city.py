class City:
    def __init__(self, *args, **kwargs):
        self.state_id = kwargs.get('state_id')
        self.city = kwargs.get('city')