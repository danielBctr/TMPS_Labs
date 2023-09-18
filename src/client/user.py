from TMPS_Labs.src.client.Account import Account


class User:
    def __init__(self, username, balance):
        self.username = username
        self.account = Account(balance)

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

