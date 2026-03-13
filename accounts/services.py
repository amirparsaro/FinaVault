from accounts.exceptions import UserDoesNotExistException
from accounts.models import User

# PRIMARY
def create_user(username: str, password: str, email: str):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def update_user(user_id: int, new_user: User): # TODO: password must have a different way
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise UserDoesNotExistException("No users found with such id")

    user.username = new_user.username
    user.email = new_user.email
    user.password = new_user.password
    user.save()
    return user

def read_user(user_id: int):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise UserDoesNotExistException("No users found with such id")

    return user

def delete_user(user_id: int):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise UserDoesNotExistException("No users found with such id")

    user.delete()

# SECONDARY
def sign_up(username: str, password: str, email: str): # throws InvalidPasswordCreation
    create_user(username, password, email)

def login(username: str, password: str): # throws UserDoesNotExist
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise UserDoesNotExistException("No users found with such username")

    if not user.check_password(password):
        raise UserDoesNotExistException("No users found with such password")

    return user

# TODO: Add Auth Table to Database