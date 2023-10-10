from TMPS_Labs.src.Factory.factory import UserFactory
from TMPS_Labs.src.MainApp.mainapp import UserRepository, AdminMenuController, UserGameController, MainMenuController, \
    GameControllerAdapter
from TMPS_Labs.src.client.admin import Admin
from TMPS_Labs.src.game.game import GameBuilder, GameProxy

if __name__ == "__main__":
    # Create Singleton instances
    admin = Admin()
    user_repository = UserRepository(admin)
    admin_menu_controller = AdminMenuController(admin)
    #Second instance that has the same variables as the first one.
    admin2 = Admin()
    user_repository2 = UserRepository(admin)
    admin_menu_controller2 = AdminMenuController(admin)

    # Create objects using Factory Methods
    user = UserFactory.create_user("John", 100, "None","Male")
    user2 = UserFactory.create_user("Alice", 1000, "None", None)

    # Create a GameBuilder using Builder pattern
    game_builder = GameBuilder(user).with_max_rounds(15).with_win_probability(0.4).with_honest_game(False)
    game = game_builder.build()

    # Use the Prototype pattern to clone a user
    john_clone = user.clone()
    john_clone.username = "John_Clone"

    # The rest of your code remains the same
    user_game_controller = UserGameController(user_repository)
    main_menu_controller = MainMenuController(user_game_controller, admin_menu_controller)

    # Create an Adapter for the Game class to make it compatible with IGameController
    game_controller_adapter = GameControllerAdapter(game)

    # Create a GameProxy instance, which will control access to the Game class
    game_proxy = GameProxy(user, max_rounds=15, win_probability=0.4, honest_game=False)

    main_menu_controller.menu()