from models import User, Game, Achievement
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import choice as rc

engine = create_engine('sqlite:///data.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()
session.query(Game).delete()
session.query(Achievement).delete()

users = {
    User(username="baby123", email="jake@blah.com"),
    User(username="pandalover", email="cool@gmail.com"),
    User(username="abc", email="123faker@yahoo.com"),
    User(username="jofff", email="john@hotmail.com"),
    User(username="heykky", email="daffyduck@masdf.com"),
    User(username="solaire123", email="Santa324@blah.com")
}

games = [
    Game(title="The Legend of Zelda: Breath of the Wild"),
    Game(title="Grand Theft Auto V"),
    Game(title="Super Mario Odyssey"),
    Game(title="The Witcher 3: Wild Hunt"),
    Game(title="Red Dead Redemption 2"),
    Game(title="Dark Souls III"),
    Game(title="Minecraft"),
    Game(title="Fortnite"),
    Game(title="Overwatch"),
    Game(title="Final Fantasy VII"),
    Game(title="Call of Duty: Modern Warfare"),
    Game(title="Assassin's Creed Valhalla"),
    Game(title="Cyberpunk 2077"),
    Game(title="Animal Crossing: New Horizons"),
    Game(title="Halo: Reach"),
    Game(title="Destiny 2"),
    Game(title="Borderlands 3"),
    Game(title="Fallout 4"),
    Game(title="God of War"),
    Game(title="The Elder Scrolls V: Skyrim")
]

achievements = {
    Achievement(title="Novice Explorer", description="Visited the first location.", status="Unlocked", type="bronze"),
    Achievement(title="Master Craftsman", description="Crafted 100 items.", status="Locked", type="silver"),
    Achievement(title="Legendary Hero", description="Completed the main storyline.", status="Locked", type="gold"),
    Achievement(title="Pacifist", description="Completed a level without harming any enemies.", status="Unlocked", type="silver"),
    Achievement(title="Treasure Hunter", description="Collected all hidden treasures.", status="Locked", type="gold"),
    Achievement(title="Completionist", description="Unlocked all achievements.", status="Locked", type="platinum")
}

for achievement in achievements:
    achievement.game = rc(games)

print(users)
print(games)
print(achievements)

session.add_all(achievements)
session.bulk_save_objects(users)
session.bulk_save_objects(games)
session.commit()