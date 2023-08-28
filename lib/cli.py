from db.models import User, Game, Achievement
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from simple_term_menu import TerminalMenu
from prettycli import red
import re
import time

class Cli():

    def __init__(self):
        current_user = None

    def main(self):
        options = ["Sign In", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Exit":
            print("Thank you for using Achievement Tracker!")
        else:
            self.sign_in()

    def sign_in(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        email = input("Please enter your email address: ")
        if(re.fullmatch(regex, email)):
            username = input("Please enter your username: ")
            # insert user into table
            user = User.find_or_create_by(username, email)
            self.current_user = user
            # go to user menu
            self.user_menu(user)
        else:
            print(red("\n\nInvalid Email. Please try again.\n\n"))
            self.main()
        


    def user_menu(self, user):
        print("\n\nMain Menu\n")
        options = ["My Game List", "My Trophies", "All Games", "Sign Out"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "My Game List":
            self.show_game_list()
        elif options[menu_entry_index] == "My Trophies":
            self.show_trophy_list()
        elif options[menu_entry_index] == "All Games":
            self.show_all_games()
        else:
            self.main()



    def show_game_list(self):
        print("My Game List\n\n")



    def show_all_games(self):
        # print all the games in the games table to the terminal
        games = Game.get_games()
        terminal_menu = TerminalMenu(
        [game.title for game in games],
        multi_select=True,
        show_multi_select_hint=True,
        )
        menu_entry_indices = terminal_menu.show()
        print(menu_entry_indices)
        print(terminal_menu.chosen_menu_entries)

        Game.append_games_to_user(self.current_user, menu_entry_indices)
        self.user_menu(self.current_user)


    def show_trophy_list(self):
        pass

if __name__ == "__main__":
    print("Welcome to Achievement Tracker!\n\n")
    app = Cli()
    app.main()