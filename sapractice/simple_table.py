from sqlalchemy import Column, Integer, String, ForeignKey, DDL
from sqlalchemy.orm import relationship, aliased

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
    session = create_session
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

    result = session.query(User).join(Habit).filter(Habit.title == 'tea').all()
    print(result)

    # result = query.join(Habit, User.id == Habit.user_id)
    # print(result)
    # --------------------------
    first_habit_alias = aliased(Habit)
    second_habit_alias = aliased(Habit)
    for user, habit1, habit2 in session.query(
            User.name, first_habit_alias.title, second_habit_alias.title
    ).join(
        first_habit_alias, User.habits
    ).join(
        second_habit_alias, User.habits
    ).filter(
        first_habit_alias.title == 'tea'
    ).filter(
        second_habit_alias.title == 'smoking'
    ):
        print(user, habit1, habit2)
