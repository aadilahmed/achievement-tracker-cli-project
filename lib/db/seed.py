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

users = [
    User(username="baby123", email="jake@blah.com"),
    User(username="pandalover", email="cool@gmail.com"),
    User(username="abc", email="123faker@yahoo.com"),
    User(username="jofff", email="john@hotmail.com"),
    User(username="heykky", email="daffyduck@masdf.com"),
    User(username="solaire123", email="Santa324@blah.com"),
    User(username="asdfasdf", email="aadilahmed0@gmail.com")
]

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

achievements = [
    Achievement(title="Novice Explorer", description="Visited the first location.", status="Unlocked", type="bronze"),
    Achievement(title="Master Craftsman", description="Crafted 100 items.", status="Locked", type="silver"),
    Achievement(title="Legendary Hero", description="Completed the main storyline.", status="Locked", type="gold"),
    Achievement(title="Pacifist", description="Completed a level without harming any enemies.", status="Unlocked", type="silver"),
    Achievement(title="Treasure Hunter", description="Collected all hidden treasures.", status="Locked", type="gold"),
    Achievement(title="Completionist", description="Unlocked all achievements.", status="Locked", type="platinum"),
    Achievement(title="Swift Runner", description="Completed a level in record time.", status="Unlocked", type="bronze"),
    Achievement(title="Dungeon Delver", description="Explored every corner of the dungeon.", status="Locked", type="silver"),
    Achievement(title="Master of Elements", description="Unleashed all elemental attacks.", status="Unlocked", type="gold"),
    Achievement(title="Stealthy Shadow", description="Successfully completed a level without being detected.", status="Locked", type="silver"),
    Achievement(title="Arena Champion", description="Emerged victorious in the arena battles.", status="Unlocked", type="gold"),
    Achievement(title="Code Breaker", description="Cracked the secret code.", status="Locked", type="bronze"),
    Achievement(title="Legendary Collector", description="Gathered all rare items.", status="Locked", type="gold"),
    Achievement(title="Jungle Explorer", description="Navigated through the treacherous jungle.", status="Locked", type="silver"),
    Achievement(title="Monster Slayer", description="Defeated all types of monsters.", status="Unlocked", type="bronze"),
    Achievement(title="Sky High", description="Reached the highest point in the game world.", status="Locked", type="silver"),
    Achievement(title="Time Traveler", description="Jumped through time portals.", status="Locked", type="gold"),
    Achievement(title="Mechanical Genius", description="Assembled the ultimate mechanical device.", status="Unlocked", type="gold"),
    Achievement(title="Master Tactician", description="Outsmarted the toughest opponents.", status="Locked", type="silver"),
    Achievement(title="Ancient Relics", description="Uncovered hidden artifacts from the past.", status="Locked", type="bronze"),
    Achievement(title="Master Alchemist", description="Brewed the rarest potions.", status="Locked", type="gold"),
    Achievement(title="Parkour Prodigy", description="Nailed every complex jump in the game.", status="Unlocked", type="silver"),
    Achievement(title="Champion of the Realm", description="Conquered all regions of the game world.", status="Locked", type="gold"),
    Achievement(title="Abyss Explorer", description="Ventured into the depths of the abyss.", status="Locked", type="silver"),
    Achievement(title="Speed Demon", description="Finished a race in record time.", status="Unlocked", type="bronze"),
    Achievement(title="Mythical Beasts", description="Encountered legendary creatures.", status="Locked", type="gold"),
    Achievement(title="Pixel Painter", description="Customized your in-game living space.", status="Unlocked", type="bronze"),
    Achievement(title="Master Hacker", description="Cracked the most complex security systems.", status="Locked", type="silver"),
    Achievement(title="Battle Royale Champion", description="Emerging victorious in the toughest battles.", status="Locked", type="gold"),
    Achievement(title="Explorer's Legacy", description="Carried on the tradition of exploration.", status="Unlocked", type="bronze"),
    Achievement(title="Cursed Encounter", description="Faced the ancient curse and survived.", status="Locked", type="silver"),
    Achievement(title="Champion Collector", description="Gathered all achievements in the game.", status="Unlocked", type="platinum"),
    Achievement(title="Music Maestro", description="Unlocked all in-game musical compositions.", status="Locked", type="silver"),
    Achievement(title="Steampunk Pioneer", description="Brought steam-powered technology to life.", status="Locked", type="bronze"),
    Achievement(title="Legendary Duelist", description="Defeated every major opponent in duels.", status="Unlocked", type="gold"),
    Achievement(title="Globetrotter", description="Visited every corner of the virtual world.", status="Locked", type="silver"),
    Achievement(title="Master Cartographer", description="Mapped out uncharted territories.", status="Locked", type="bronze"),
    Achievement(title="Mythical Historian", description="Unveiled the secrets of ancient myths.", status="Unlocked", type="gold"),
    Achievement(title="Benevolent Savior", description="Helped all NPCs with their troubles.", status="Locked", type="silver"),
    Achievement(title="Aerial Acrobat", description="Performed death-defying stunts in the sky.", status="Locked", type="bronze")
]

i = 0
for game in games:
    game.achievements.append(achievements[i])
    game.achievements.append(achievements[i+1])
    i+=2


session.add_all(achievements)
session.add_all(users)
session.add_all(games)
session.commit()