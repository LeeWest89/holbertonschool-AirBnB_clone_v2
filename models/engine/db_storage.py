#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

all_classes = {"State", "City", "Amenity", "User", "Place", "Review"}


class DBStorage:
    """DB storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """connects MYSQL DB"""

        db_uri = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB'))

        self.__engine = create_engine(db_uri, pool_pre_ping=True)
        self.reload()

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """defilnes all"""
        entities = dict()

        if cls:
            return self.get_data_from_table(cls, entities)

        for entity in all_classes:
            entities = self.get_data_from_table(eval(entity), entities)

        return entities

    def new(self, obj):
        """Add obj to the current DB."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """save and commit"""

        self.__session.commit()

    def delete(self, obj=None):
        """Deletes Objects"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """initializes created tables in DB."""

        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def get_data_from_table(self, cls, structure):
        """Gather data from MySQL Table"""

        if type(structure) is dict:
            query = self.__session.query(cls)

            for _row in query.all():
                key = "{}.{}".format(cls.__name__, _row.id)
                structure[key] = _row

            return structure

    def close(self):
        """closes current session"""
        self.__session.remove()
