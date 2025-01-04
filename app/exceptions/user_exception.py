class UserNotFound(Exception):
	def __init__(self, message: str = None):
		self.message = message
		super().__init__(self.message)


class UserAlreadyExists(Exception):
	def __init__(self, message: str = None):
		self.message = message
		super().__init__(self.message)
