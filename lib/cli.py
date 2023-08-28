from db.models import User, Game, Achievement
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from simple_term_menu import TerminalMenu

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
        email = input("Please enter your email address: ")
        username = input("Please enter a username:")
        password = input("Please enter a password:")
        """ insert new user into User table """
        new_user = User(username=username, email=email)
    

    def sign_in(self):
        username = input("Username: ")
        password = input("Password: ")

    def user_menu(self):
        options = ["My Game List", "My Trophies" "All Games", "Sign Out"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")

if __name__ == "__main__":
    print("Welcome to Achievement Tracker!\n\n")
    app = Cli()
    app.main()