
def validate_username(username):
    if not username:
        return False, "Username cannot be empty"
    if len(username) < 3:
        return False, "Username too short"
    return True, "OK"

def validate_password(password):
    if not password:
        return False, "Password cannot be empty"
    if len(password) < 4:
        return False, "Password too short"
    return True, "OK"