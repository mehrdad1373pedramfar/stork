from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from sapractice.config import base, create_session, metadata


class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    habits = relationship('Habit', back_populates='user')

    def __repr__(self):
        return self.name


class Habit(base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    reward = Column(String)

    user = relationship('User', back_populates='habits')

    user_id = Column(Integer, ForeignKey(User.id))

    def __repr__(self):
        return self.title


if __name__ == '__main__':
    session = create_session()
    metadata.create_all()
    users = list()
    for i in range(10):
        users.append(User(name=f'User{i}'))
    session.add_all(users)
    session.commit()
    users[0].name = 'mhr'
    print(session.new)
    print(session.dirty)
    # --------------------------------------
    for u in session.query(User):
        print(u)

    # user = session.query(User).filter_by(name='mhr').one()
    # print(user)

    for u in session.query(User).filter(User.name.in_(['User0', 'User2'])):
        print(u)
    # -------------------------------------

    habits = list()
    for i in range(5):
        users[0].habits.append(Habit(title='smoking', reward='some reward'))

    session.commit()
    #
    user = session.query(User).filter(User.name == 'mhr').one()
    print(user.habits)

    user.habits[2] = Habit(title="tea", reward="another reward")
    print(user.habits)
    session.commit()
