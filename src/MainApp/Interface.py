from abc import ABC, abstractmethod

# Interface for a Game
class IGame(ABC):
    @abstractmethod
    def end_round(self, amount):
        pass


# Interface for a User
class IUser(ABC):
    @abstractmethod
    def play(self, game, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def view_stats(self):
        pass

# Adapter for IUser to make it compatible with IGame
class IUserAdapter(IGame):
    def __init__(self, user):
        self.user = user

    def end_round(self, amount):
        return self.user.play(self, amount)

# Example implementation of IUser and IGame
class User1(IUser):
    def play(self, game, amount):
        result = game.end_round(amount)
        return result

class CasinoGame(IGame):
    def end_round(self, amount):

        return 42  # Example result