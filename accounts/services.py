from django.contrib.auth import get_user_model, authenticate, login, logout
from django.utils import timezone
from accounts.exceptions import *

User = get_user_model()

def create_user(username: str, password: str, email: str):
    if User.objects.filter(username=username).exists():
        raise UserAlreadyExistsException("This username already exists")

    if User.objects.filter(email=email).exists():
        raise UserAlreadyExistsException("This email already exists")

    return User.objects.create_user(
        username=username,
        email=email,
        password=password,
    )

def update_user(user_id: int, new_user: User):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise UserDoesNotExistException("No users found with such id")

    if user.username is not None:
        try:
            User.objects.get(username=new_user.username)
        except User.DoesNotExist:
            user.username = new_user.username

        raise UserAlreadyExistsException("This username already exists")

    if user.email is not None:
        try:
            User.objects.get(email=new_user.email)
        except User.DoesNotExist:
            user.email = new_user.email

        raise EmailAlreadyExistsException("This email already exists")

    if new_user.password:
        user.set_password(new_user.password)

    user.save()
    return user

def read_user(user_id: int):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise UserDoesNotExistException("No users found with such id")

def delete_user(user_id: int):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise UserDoesNotExistException("No users found with such id")

    user.delete()

def register_user(username: str, password: str, email:str):
    return create_user(username=username, password=password, email=email)

def login_user(request, username: str, password: str):
    user = authenticate(request, username, password)

    if user is None:
        raise InvalidCredentialsException("Invalid username or password")

    login(request, user)
    return user

def logout_user(request):
    logout(request) # In Views, return error code 401 (unauthorized)
