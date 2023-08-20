from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()

users = {
    User(username="baby123", email="jake@blah.com"),
    User(username="pandalover", email="cool@gmail.com"),
    User(username="abc", email="123faker@yahoo.com"),
    User(username="jofff", email="john@hotmail.com"),
    User(username="heykky", email="daffyduck@masdf.com"),
    User(username="solaire123", email="Santa324@blah.com")
}

print(users)

session.bulk_save_objects(users)
session.commit()