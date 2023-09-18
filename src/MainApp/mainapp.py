from TMPS_Labs.src.game.game import Game


class UserManagement:
    def __init__(self, admin):
        self.admin = admin

    def start_user_game(self, username):
        user = self.admin.find_user(username)
        if user is None:
            print("User not found. Creating a new user...")
            user = self.admin.create_user(username)
        game = Game(user)
        game.play_game()


class AdminMenu:
    def __init__(self, admin):
        self.admin = admin

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Create User")
            print("2. Manage User")
            print("3. Back to Main Menu")

            admin_choice = input("Enter your choice: ")

            if admin_choice == "1":
                username = input("Enter the username for the new user: ")
                self.admin.create_user(username)
                print(f"User '{username}' created.")

            elif admin_choice == "2":
                self.admin.manage_user()

            elif admin_choice == "3":
                break

            else:
                print("Invalid choice. Please select a valid option.")


class MenuManagement:
    def __init__(self, user_management, admin_menu):
        self.user_management = user_management
        self.admin_menu = admin_menu

    def start_game(self):
        while True:
            print("\nChoose an option:")
            print("1. Play as User")
            print("2. Play as Admin")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter your username: ")
                self.user_management.start_user_game(username)

            elif choice == "2":
                self.admin_menu.admin_menu()

            elif choice == "3":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")
