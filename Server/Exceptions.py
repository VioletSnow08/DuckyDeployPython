class InvalidClientId(Exception):
    def __init__(self, id_arg):
        self.id = id_arg