#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.engine.db_storage import DBStorage
import MySQLdb


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "FileStorage Mode")
class TestFileStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        storage = DBStorage()
        state = State(name="Cundinamarca")
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        db = MySQLdb.connect(host=HBNB_MYSQL_HOST, user=HBNB_MYSQL_USER,
                             passwd=HBNB_MYSQL_PWD, db=HBNB_MYSQL_DB)
        cursor = db.cursor()
        state.save()
        storage.save()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user
        del cls.state
        self.cursor.close()
        self.db.close()

    def tearDown(self):
        """teardown"""
        try:
            query = """
            DROP TABLE IF EXIST amenities;
            DROP TABLE IF EXIST cities;
            DROP TABLE IF EXIST place_amenity;
            DROP TABLE IF EXIST reviews;
            DROP TABLE IF EXIST states;
            DROP TABLE IF EXIST users;
            """
            self.cursor.execute(query)
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in File Storage"""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._DBStorage__objects)

if __name__ == "__main__":
    unittest.main()
