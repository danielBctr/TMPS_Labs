from TMPS_Labs.src.MainApp.mainapp import UserManagement, AdminMenu, MenuManagement
from TMPS_Labs.src.client.admin import Admin

if __name__ == "__main__":
    admin = Admin()
    user_management = UserManagement(admin)
    admin_menu = AdminMenu(admin)
    menu_management = MenuManagement(user_management, admin_menu)
    menu_management.start_game()
