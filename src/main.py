from TMPS_Labs.src.MainApp.GamblingFacade import *

if __name__ == "__main__":
    ## Lab2
    # Create Singleton instances
    admin = Admin()
    user_repository = UserRepository(admin)
    admin_menu_controller = AdminMenuController(admin)
    # Second instance that has the same variables as the first one.
    admin2 = Admin()
    user_repository2 = UserRepository(admin)
    admin_menu_controller2 = AdminMenuController(admin)

    # Create objects using Factory Methods
    user = UserFactory.create_user("John", 100, "None", "Male")
    user2 = UserFactory.create_user("Alice", 1000, "None", None)

    # Create a GameBuilder using Builder pattern
    game_builder = GameBuilder(user).with_max_rounds(15).with_win_probability(0.4).with_honest_game(False)
    game = game_builder.build()

    # Use the Prototype pattern to clone a user
    john_clone = user.clone()
    john_clone.username = "John_Clone"

    user_game_controller = UserGameController(user_repository)
    main_menu_controller = MainMenuController(user_game_controller, admin_menu_controller)
    ## Lab3
    # Create an Adapter for User, so he can use the IGame functions
    user_adapter = IUserAdapter(user)

    # Create a GameProxy instance, which will control access to the Game class
    game_proxy = GameProxy(user, max_rounds=10, win_probability=0.1, honest_game=False)

    # Use of decorator
    gambling_machine = GamblingMachine()
    gambling_machine.print_screen()
    main_menu_controller.menu()

    ##Lab4