from db.models import User, Game, Achievement
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from simple_term_menu import TerminalMenu
from prettycli import red
import re

class Cli():

    def main(self):
        options = ["Sign In", "Create Account", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Exit":
            print("Thank you for using Achievement Tracker!")
        elif options[menu_entry_index] == "Create Account":
            self.create_account()
        else:
            self.sign_in()

    def create_account(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        email = input("Please enter your email address: ")
        if(re.fullmatch(regex, email)):
            username = input("Please enter a username:")
            password = input("Please enter a password:")
            # insert user into table
            new_user = User.find_or_create_by(username, email)
            # go to user menu
            self.user_menu()
        else:
            print(red("\n\nInvalid Email. Please try again.\n\n"))
            self.main()
    

    def sign_in(self):
        username = input("Username: ")
        password = input("Password: ")

    def user_menu(self):
        options = ["My Game List", "My Trophies", "All Games", "Sign Out"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "My Game List":
            print("My Game List")
        elif options[menu_entry_index] == "My Trophies":
            print("My Trophies")
        elif options[menu_entry_index] == "All Games":
            print("All Games")
        else:
            print("Thank you for using Achievement Tracker!")
            self.main()

if __name__ == "__main__":
    print("Welcome to Achievement Tracker!\n\n")
    app = Cli()
    app.main()