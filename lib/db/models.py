from sqlalchemy import Column, Integer, String, Table, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///db/data.db')

Session = sessionmaker(bind=engine)
session = Session()

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

    @classmethod
    def find_or_create_by(cls, username, email):
        user = session.query(cls).filter(cls.email.like(email)).first()
        if user:
            return user
        else:
            user = User(username=username, email=email)
            session.add(user)
            session.commit()
            return user

    def __repr__(self):
        return f"\n<User " + \
            f"id={self.id}, " + \
            f"username={self.username}, " + \
            f"email={self.email}, " \
            + ">"
    
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String)

    users = relationship('User', secondary=user_game, back_populates='games')
    achievements = relationship('Achievement', backref='game')

    @classmethod
    def get_games(cls):
        games = session.query(cls).all()
        return games
    
    @classmethod
    def append_games_to_user(cls, user, game_ids):
        for id in game_ids:
            game = session.query(cls).filter(cls.id == id+1).first()
            if game not in user.games:
                user.games.append(game)
        session.commit()

    def __repr__(self):
        return f"\n<Game " + \
            f"id={self.id}, " + \
            f"title={self.title}, " \
            + ">"
    
class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer(), primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    type = Column(String)
    game_id = Column(Integer(), ForeignKey('games.id'))

    def __repr__(self):
        return f"\n<Achievement " + \
            f"id={self.id}, " + \
            f"title={self.title}, " + \
            f"description={self.description}, " + \
            f"status={self.status}, " + \
            f"type={self.type}, " \
            + ">"
        