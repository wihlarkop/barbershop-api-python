class TokenExpired(Exception):
    def __init__(self, message: str = None):
        self.message = message
        super().__init__(self.message)


class TokenInvalid(Exception):
    def __init__(self, message: str = None):
        self.message = message
        super().__init__(self.message)