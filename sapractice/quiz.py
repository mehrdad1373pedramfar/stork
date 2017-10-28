
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property

from sapractice.config import base, create_session, metadata


class Person(base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    _first_name = Column(String)
    _last_name = Column(String)
    role = Column(String)

    __mapper_args__ = {
        'polymorphic_identity':  __tablename__,
        'polymorphic_on': role
    }

    @hybrid_property
    def name(self):
        return self._first_name + ' - ' + self._last_name

    @name.setter
    def name(self, name):
        self._first_name, self._last_name = name.split(' ')

    def __repr__(self):
        return f'{self.id} {self.name} ({self.role})'


class Admin(Person):
    __tablename__ = 'admin'

    id = Column(Integer, ForeignKey('person.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':  __tablename__,
    }


class Doctor(Person):
    __tablename__ = 'doctor'

    id = Column(Integer, ForeignKey('person.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':  __tablename__,
    }


class Patient(Person):
    __tablename__ = 'patient'

    id = Column(Integer, ForeignKey('person.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':  __tablename__,
    }


if __name__ == '__main__':
    session = create_session()
    metadata.create_all()
    session.add(Doctor(name='mehrdad pedramfar'))
    session.add(Person(name='armin ayari'))
    session.commit()

    print('Doctors: ')
    for d in session.query(Doctor).all():
        print(d)

    print('Persons: ')
    for p in session.query(Person).all():
        print(p)

    doc = session.query(Doctor).filter(Doctor.name == 'mehrdad - pedramfar').one_or_none()
    print(doc)
    per = session.query(Person).filter(Person.name == 'armin - ayari').one_or_none()
    print(per)
