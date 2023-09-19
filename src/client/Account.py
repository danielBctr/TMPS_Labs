class Account:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.winnings = 0
        self.losses = 0

    def add_winnings(self, amount):
        self.winnings += amount
        self.balance += amount

    def add_losses(self, amount):
        self.losses += amount
        self.balance -= amount

    def check_balance(self):
        return self.balance

#Liskov Substitution
class EnhancedAccount(Account):
    def __init__(self, initial_balance=1000):
        super().__init__(initial_balance)
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def view_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)
