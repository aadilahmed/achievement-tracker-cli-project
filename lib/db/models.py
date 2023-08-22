from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()

user_game = Table(
    'user_games',
    Base.metadata,
    Column('game_id', ForeignKey('games.id'), primary_key=True),
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    extend_existing=True,
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String)
    email = Column(String(55))

    games = relationship('Game', secondary=user_game, back_populates='users')

    def __repr__(self):
        return f"\n<User" + \
            f"id={self.id}, " + \
            f"username={self.username}, " + \
            f"email={self.email}, " \
            + ">"
    
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String)

    users = relationship('User', secondary=user_game, back_populates='games')

    def __repr__(self):
        return f"\n<Game" + \
            f"id={self.id}, " + \
            f"title={self.title}, " + \
            + ">"
    

class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer(), primary_key=True)
    title = Column(String)

    def __repr__(self):
        return f"\n<Achievement" + \
            f"id={self.id}, " + \
            f"title={self.title}, " + \
            + ">"
        