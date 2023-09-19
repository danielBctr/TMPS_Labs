from TMPS_Labs.src.MainApp.mainapp import UserRepository, AdminMenuController, UserGameController, MainMenuController
from TMPS_Labs.src.client.admin import Admin

if __name__ == "__main__":
    admin = Admin()
    user_repository = UserRepository(admin)
    user_game_controller = UserGameController(user_repository)
    admin_menu_controller = AdminMenuController(admin)
    main_menu_controller = MainMenuController(user_game_controller, admin_menu_controller)

    main_menu_controller.menu()
