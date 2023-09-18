from abc import ABC, abstractmethod


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


class MainAppInterface(IUserGameController, IAdminMenuController, ABC):
    pass
