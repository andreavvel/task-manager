# authentication/utils.py
def is_admin(user):
    return user.is_authenticated and user.is_admin

def is_regular_user(user):
    return user.is_authenticated and not user.is_admin
