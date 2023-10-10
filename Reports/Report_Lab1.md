# Laboratory work Nr.1

### Course: TMPS
### Author: Bucătaru Daniel, FAF-211


----

## Theory
The SOLID principles are a set of guidelines for writing clean and maintainable code:

1. Single Responsibility Principle (SRP): Each class should have one responsibility, making code easier to understand and maintain.

2. Open-Closed Principle (OCP): Software entities should be open for extension but closed for modification, allowing for easy updates without altering existing code.

3. Liskov Substitution Principle (LSP): Derived classes should seamlessly replace base classes without changing program behavior, ensuring consistent behavior.

4. Interface Segregation Principle (ISP): Create specific interfaces for classes, avoiding unnecessary method implementations and reducing coupling.

5. Dependency Inversion Principle (DIP): Depend on abstractions, not concrete implementations, for flexibility and easy component substitution.

6. These principles promote modular, flexible, and robust software design.

----
## Objectives:

 1. Study and understand the SOLID Principles.

2. Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms.

3. Create a sample project that respects SOLID Principles.


----
## Implementation description

 I have 3 directories client, game and Mainapp, and i have the main.py where all are combined
this is a good example of interface segregation.
````
if __name__ == "__main__":
    admin = Admin()
    user_repository = UserRepository(admin)
    user_game_controller = UserGameController(user_repository)
    admin_menu_controller = AdminMenuController(admin)
    main_menu_controller = MainMenuController(user_game_controller, admin_menu_controller)

    main_menu_controller.menu()
  
````
 Here are the abstract classes that all the code is based on
````
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
````
The single responsibility, all classes do just one thing.
 
````
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
````
----
## Conclusions / Screenshots / Results
### Screenshots/Results:

----
### Conclusion:
   In conclusion, the SOLID principles represent a set of fundamental guidelines and 
   best practices for designing maintainable, flexible, and robust software systems. 
   These principles, which include Single Responsibility, Open/Closed, 
   Liskov Substitution, Interface Segregation, and Dependency Inversion, 
   serve as a cornerstone for object-oriented design and development. 
   When applied effectively, SOLID principles lead to code that is easier 
   to understand, modify, and extend, reducing the likelihood of bugs and making 
   software systems more adaptable to change.
----
## References

https://github.com/DrVasile/FLFA-Labs/blob/master/1_RegularGrammars/task.md 
