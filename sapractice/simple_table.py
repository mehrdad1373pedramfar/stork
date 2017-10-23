from sqlalchemy import Column, Integer, String

from sapractice.config import base, create_session, metadata


class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return self.name


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

    user = session.query(User).filter_by(name='User1').first()
    print(user)

    for u in session.query(User).filter(User.name.in_(['User1', 'User2'])):
        print(u)
