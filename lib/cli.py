from db.models import User, Game, Achievement
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from simple_term_menu import TerminalMenu
from prettycli import red, green
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
            self.clear_terminal()
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
        print("\n\nMy Game List\n\n")
        games = self.current_user.games
        options = [game.title for game in games]
        options.append("Back")
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Back":
            self.user_menu(self.current_user)
        else:
            self.show_game_achievements(options[menu_entry_index])

    def show_all_games(self):
        # print all the games in the games table to the terminal
        games = Game.get_all_games()
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

    def show_game_achievements(self, game):
        print(f"\n\n{game} Achievements\n")
        achievements = Game.get_all_achievements(game)
        options = [achievement.title for achievement in achievements]
        options.append("Back")
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Back":
            self.show_game_list()
        else:
            self.display_achievement_info(options[menu_entry_index], game)

    def display_achievement_info(self, title, game):
        achievement = Achievement.find_by_title(title)
        status = ""
        if achievement.status == "Unlocked":
            status = green(f"{achievement.status}")
        else:
            status = red(f"{achievement.status}")
                    
        print(f"{achievement.title} : " + status) 
        print(f"{achievement.description}") 

        options = ["Lock/Unlock Achievement", "Back"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Back":
            self.show_game_achievements(game)
        else:
            # change status
            if achievement.status == "Unlocked":
                achievement.status = "Locked"
            else:
                achievement.status = "Unlocked"
            # return to achievement info page
            self.display_achievement_info(title, game)
            


    def clear_terminal(self):
        print("\n" * 30)   

    def show_trophy_list(self):
        pass

if __name__ == "__main__":
    print("Welcome to Achievement Tracker!\n\n")
    app = Cli()
    app.main()