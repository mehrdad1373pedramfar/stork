
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property

from sapractice.config import base, create_session, metadata


class Person(base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String)

    __mapper_args__ = {
        'polymorphic_identity':  __tablename__,
        'polymorphic_on': role
    }

    @hybrid_property
    def name(self):
        return self.first_name + ' ' + self.last_name

    @name.setter
    def name(self, name):
        self.first_name, self.last_name = name.split(' ')

    def __repr__(self):
        return f'{self.id} {self.first_name} - {self.last_name} ({self.role})'


class Admin(Person):
    __mapper_args__ = {
        'polymorphic_identity':  'admin'
    }


class Doctor(Person):
    __mapper_args__ = {
        'polymorphic_identity':  'doctor'
    }


class Patient(Person):
    __mapper_args__ = {
        'polymorphic_identity':  'patient'
    }


if __name__ == '__main__':
    session = create_session()
    metadata.create_all()
    session.add(Doctor(name='mehrdad pedramfar'))
    session.add(Person(name='armin ayari'))
    session.commit()

    print('Doctors: ')
    for d in session.query(Doctor):
        print(d)

    print('Persons: ')
    for p in session.query(Person):
        print(p)

    doc = session.query(Doctor).filter(Doctor.name == 'mehrdad pedramfar').one_or_none()
    print(doc)
    per = session.query(Person).filter(Person.name == 'armin ayari').one_or_none()
    print(per)
