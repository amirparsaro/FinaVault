class InvalidPasswordCreationException(Exception):
    pass

class UserDoesNotExistException(Exception):
    pass

class UserAlreadyExistsException(Exception):
    pass

class TokenDoesNotExistException(Exception):
    pass

class EmailAlreadyExistsException(Exception):
    pass

class InvalidCredentialsException(Exception):
    pass