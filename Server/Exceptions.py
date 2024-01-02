class InvalidClientId(Exception):
    def __init__(self, id_arg):
        self.id = id_arg


class InvalidArguments(Exception):
    def __init__(self, arg_error):
        self.argumentError = arg_error
