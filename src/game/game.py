import random


class IGame:
    def play_round(self, amount):
        pass

    def play_game(self):
        pass

class Game(IGame):
    def __init__(self, user, max_rounds=10, win_probability=0.3, honest_game=True):
        self.user = user
        self.lost_all_money = False
        self.max_rounds = max_rounds
        self.win_probability = win_probability
        self.honest_game = honest_game

    def play_round(self, amount):

        win_probability = 0.3
        if random.random() < win_probability:
            result = amount // 2
        else:
            result = -amount

        if result > 0:
            self.user.account.add_winnings(result)
            print(f"Congratulations! You won {result}.")
        else:
            self.user.account.add_losses(-result)
            print(f"Sorry, you lost {amount}.")

        if self.user.check_balance() <= 0:
            self.lost_all_money = True

        return result

    def play_game(self):
        print("Welcome to the Gambling Machine!")
        while True:
            if self.lost_all_money:
                print("You've lost all your money. Game over.")
                break

            print("\nChoose an option:")
            print("1. Play")
            print("2. Check Balance")
            print("3. View Stats")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    amount = int(input("Enter the amount to bet: "))
                    if amount <= self.user.check_balance():
                        result = self.play_round(amount)
                    else:
                        print("Insufficient balance. Please enter a valid amount.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")

            elif choice == "2":
                balance = self.user.check_balance()
                print(f"Your balance: {balance}")

            elif choice == "3":
                self.user.view_stats()

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")
class GameBuilder:
    def __init__(self, user):
        self.user = user
        self.max_rounds = 10
        self.win_probability = 0.3
        self.honest_game = True

    def with_max_rounds(self, max_rounds):
        self.max_rounds = max_rounds
        return self

    def with_win_probability(self, win_probability):
        self.win_probability = win_probability
        return self

    def with_honest_game(self, honest_game):
        self.honest_game = honest_game
        return self

    def build(self):
        return Game(self.user, self.max_rounds, self.win_probability, self.honest_game)

class GameProxy(IGame):
    def __init__(self, user, max_rounds=10, win_probability=0.3, honest_game=True):
        self.game = Game(user, max_rounds, win_probability, honest_game)

    def play_round(self, amount):
        # You can add logic here to control access or add additional functionality
        return self.game.play_round(amount)

    def play_game(self):
        # You can add logic here to control access or add additional functionality
        self.game.play_game()