from colorama import Fore, Style

def login_required(func):
    """Checks if a user is logged in."""
    def wrapper(current_user, *args, **kwargs):
        if current_user is None:
            print(Fore.RED + "Error: You must login first!" + Style.RESET_ALL)
            return # Stop the function
        return func(current_user, *args, **kwargs)
    return wrapper

def admin_required(func):
    """Checks if the user is an Admin."""
    def wrapper(current_user, *args, **kwargs):
        if current_user is None:
            print(Fore.RED + "Error: Login required." + Style.RESET_ALL)
            return
        if current_user.role != 'admin':
            print(Fore.RED + "Error: Admins only." + Style.RESET_ALL)
            return
        return func(current_user, *args, **kwargs)
    return wrapper