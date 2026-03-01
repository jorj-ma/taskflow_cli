import sys

from services.auth_service import register_user, login_user
from services.task_service import create_task, delete_task, get_task_by_user
from utilities.helpers import save_data, load_data
from utilities.validators import validate_username, validate_password
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
                    
                    user = login_user(u, p)  # returns a User object
                    if user:
                        current_user = user
                        print(Fore.GREEN + f"Login successful!\nWelcome {u}!" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Login failed." + Style.RESET_ALL)

                elif choice == "2":
                    u = input("Username: ")
                    e = input("Email: ")
                    p = input("Password: ")
                    r = input("Role (admin/user): ")

                    is_ok, msg = validate_username(u)
                    if not is_ok:
                        print(Fore.RED + msg + Style.RESET_ALL)
                        continue
                    
                    is_ok, msg = validate_password(p) 
                    if not is_ok: 
                        print(Fore.RED + msg + Style.RESET_ALL) 
                        continue
                    
                    result = register_user(u, e, p, r)
                    print(Fore.GREEN + result + Style.RESET_ALL)

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
                    tasks = get_task_by_user(current_user.email)
                    for t in tasks:
                        print(f"ID: {t.id} | {t.title} | {t.status}")

                elif choice == "2":
                    current_user = None
                
                elif choice == "3" and current_user.role == "admin":
                    title = input("Title: ")
                    desc = input("Description: ")
                    create_task(title, desc, current_user.email)
                    print("Task added.")

                elif choice == "4" and current_user.role == "admin":
                    title = input("Title to delete: ")
                    result = delete_task(title, current_user.email)
                    print(result)

                elif choice == "3" and current_user.role == "user":
                    title = input("Title of task to finish: ")
                    tasks = get_task_by_user(current_user.email)
                    for t in tasks:
                        if t.title == title:
                            t.mark_complete()
                            data = load_data()
                            for i, task_dict in enumerate(data["tasks"]):
                                if task_dict["title"] == title and task_dict["assigned_to"] == current_user.email:
                                    data["tasks"][i] = t.to_dict()
                            save_data(data)
                            print("Task finished.")
                            break
                    else:
                        print("Task not found.")

        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()