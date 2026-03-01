import sys

from services.auth_service import AuthService
from services.task_service import TaskService


from utilities.validators import validate_username, validate_password
from utilities.decorators import login_required, admin_required
from colorama import Fore, Style, init


init()

def main():
    
    current_user = None

    
    while True:
        try:
            
            if current_user is None:
                print(Fore.CYAN + "\n=== WELCOME ===" + Style.RESET_ALL)
                print("1. Login")
                print("2. Register")
                print("3. Exit")
                
                choice = input("Choice: ")

                if choice == "1":
                    u = input("Username: ")
                    p = input("Password: ")
                    
                    user = AuthService.login(u, p)
                    if user:
                        current_user = user
                        print(Fore.GREEN + f"Welcome {user.username}!" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Login failed." + Style.RESET_ALL)

                elif choice == "2":
                    u = input("Username: ")
                    p = input("Password: ")
                    r = input("Role (admin/member): ")

                    
                    is_ok, msg = validate_username(u)
                    if not is_ok:
                        print(Fore.RED + msg + Style.RESET_ALL)
                        continue
                    
                    
                    AuthService.register(u, p, r)
                    print(Fore.GREEN + "Success!" + Style.RESET_ALL)

                elif choice == "3":
                    print("Goodbye!")
                    sys.exit()

            
            else:
                print(Fore.MAGENTA + f"\n--- Dashboard ({current_user.role}) ---" + Style.RESET_ALL)
                print("1. View Tasks")
                print("2. Logout")
                
                
                if current_user.role == "admin":
                    print("3. Add Task")
                    print("4. Delete Task")
                else:
                    print("3. Finish Task")

                choice = input("Choice: ")

                if choice == "1":
                    
                    tasks = TaskService.list_tasks()
                    for t in tasks:
                        print(f"ID: {t['id']} | {t['title']} | {t['status']}")

                elif choice == "2":
                    current_user = None
                
                
                elif choice == "3" and current_user.role == "admin":
                    title = input("Title: ")
                    TaskService.create_task(title)
                    print("Task added.")

                elif choice == "4" and current_user.role == "admin":
                    tid = input("ID to delete: ")
                    TaskService.delete_task(tid)
                    print("Task deleted.")

                
                elif choice == "3" and current_user.role == "member":
                    tid = input("ID to finish: ")
                    TaskService.complete_task(tid)
                    print("Task finished.")

        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()