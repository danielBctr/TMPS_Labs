from abc import ABC, abstractmethod
from TMPS_Labs.src.game.game import Game

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class IGame(ABC):
    @abstractmethod
    def play_game(self):
        pass
class IUserRepository(ABC):
    @abstractmethod
    def find_user(self, username):
        pass

    @abstractmethod
    def create_user(self, username):
        pass


class IGameController(ABC):
    @abstractmethod
    def start_game(self, username):
        pass


class IMenuController(ABC):
    @abstractmethod
    def menu(self):
        pass


# Implement the abstractions with concrete classes
class UserRepository(metaclass=SingletonMeta):
    def __init__(self, admin):
        self.admin = admin

    def find_user(self, username):
        return self.admin.find_user(username)

    def create_user(self, username):
        return self.admin.create_user(username)


class UserGameController(IGameController):
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def start_game(self, username):
        user = self.user_repository.find_user(username)
        if user is None:
            print("User not found. Creating a new user...")
            user = self.user_repository.create_user(username)
        game = Game(user)
        game.play_game()


class AdminMenuController(metaclass=SingletonMeta):
    def __init__(self, admin):
        self.admin = admin

    def menu(self):
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

class MainMenuController(IMenuController):
    def __init__(self, user_game_controller, admin_menu_controller):
        self.user_game_controller = user_game_controller
        self.admin_menu_controller = admin_menu_controller

    def menu(self):
        while True:
            print("\nChoose an option:")
            print("1. Play as User")
            print("2. Play as Admin")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter your username: ")
                self.user_game_controller.start_game(username)

            elif choice == "2":
                self.admin_menu_controller.menu()

            elif choice == "3":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")
class GameControllerAdapter(IGameController):
    def __init__(self, game):
        self.game = game

    def start_game(self, username):
        self.game.play_game()