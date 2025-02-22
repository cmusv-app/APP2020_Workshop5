from models.User import User


def create_user(email: str, password_hash: str):
    new_user = User(email=email, password_hash=password_hash)
    new_user.save()


def find_user_by_email(email: str):
    return User.objects.filter(email=email).first()


def find_user_by_id(user_id: str):
    the_user = User.objects.get(id=user_id)
    return the_user
