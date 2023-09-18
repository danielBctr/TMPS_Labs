from TMPS_Labs.src.client.Account import Account
from TMPS_Labs.src.client.user import User


class Admin:
    def __init__(self):
        self.users = []

    def create_user(self, username, balance=1000):
        user = User(username, balance)
        self.users.append(user)
        return user

    def manage_user(self):
        # Implement methods for managing user data (reset balance, view stats...)
        username = input("Enter the username of the user to manage: ")
        user = self.find_user(username)
        if user:
            while True:
                print("\nManage User Menu:")
                print(f"User: {user.username}")
                print("1. Reset Balance")
                print("2. View Stats")
                print("3. Back to Admin Menu")

                manage_choice = input("Enter your choice: ")

                if manage_choice == "1":
                    user.account = Account()
                    print("User balance reset.")

                elif manage_choice == "2":
                    user.view_stats()

                elif manage_choice == "3":
                    break

                else:
                    print("Invalid choice. Please select a valid option.")
        else:
            print("User not found.")

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
