from TMPS_Labs.src.client.Account import Account

class UserFactory:
    @staticmethod
    def create_user(username, balance, luck, gender):
        return User(username, balance, luck, gender)

class User:
    def __init__(self, username, balance, luck, gender):
        self.username = username
        self.account = Account(balance)
        self.luck = luck
        self.gender = gender


    def play(self, game, amount):
        result = game.play_round(amount)
        if result > 0:
            print("Congratulations! You won.")
        else:
            print("Sorry, you lost.")

    def check_balance(self):
        return self.account.check_balance()

    def view_stats(self):
        print(f"Username: {self.username}")
        print(f"Balance: {self.account.check_balance()}")
        print(f"Total Winnings: {self.account.winnings}")
        print(f"Total Losses: {self.account.losses}")

    def clone(self):
        return User(self.username, self.account.balance, self.luck, self.gender)
