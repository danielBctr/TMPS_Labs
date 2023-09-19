from abc import ABC, abstractmethod

# Interface Segregation Each class only implements the
# methods that are relevant to its specific responsibilities.
class IUserGameController(ABC):
    @abstractmethod
    def start_game(self):
        pass


class IAdminMenuController(ABC):
    @abstractmethod
    def create_user(self, username):
        pass

    @abstractmethod
    def manage_user(self):
        pass


class UserGameController(IUserGameController):
    def start_game(self):
        print("Starting the game...")


class AdminMenuController(IAdminMenuController):
    def __init__(self):
        self.users = []

    def create_user(self, username):
        print(f"Creating a new user: {username}")
        self.users.append(username)

    def manage_user(self):
        if not self.users:
            print("No users to manage.")
            return

        print("Managing a user...")
        print("Select a user to manage:")
        for idx, username in enumerate(self.users, start=1):
            print(f"{idx}. {username}")

        try:
            choice = int(input("Enter the user number to manage: "))
            if 1 <= choice <= len(self.users):
                print(f"Managing user: {self.users[choice - 1]}")
            else:
                print("Invalid user selection.")
        except ValueError:
            print("Invalid input. Please enter a valid user number.")
