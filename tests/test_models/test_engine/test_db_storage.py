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
from models.engine.db_storage import DBStorage
from models import storage
import MySQLdb


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "FileStorage Mode")
class TestFileStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        db = MySQLdb.connect(host=HBNB_MYSQL_HOST, user=HBNB_MYSQL_USER,
                             passwd=HBNB_MYSQL_PWD, db=HBNB_MYSQL_DB)
        cursor = db.cursor()

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

    def test_instances(self):
        """Test if instance are saved"""
        state = State(name="California")
        storage.new(state)
        state.save()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)

    def test_db_delete(self):
        """tests if all works in File Storage"""
        state_instance = State(name="California")
        self.assertIsNotNone(state_instance)
        storage.new(state_instance)
        storage.save()
        obj_state = storage.all("State")
        self.assertEqual(len(obj_state), 3)
        storage.delete(state_instance)
        obj_state = storage.all("State")
        self.assertEqual(len(obj_state), 2)

    def test_new(self):
        """test when new is created"""
        user = User(email="gui@hbtn.io", password="guipwd",
                    first_name="Guillaume", last_name="Snow")
        user_id = user.id
        storage.new(user)
        storage.save()
        obj = storage.all()
        key = user.__class__.__name__ + "." + user_id
        self.assertIsNotNone(obj[key])

    def test_amenity(self):
        """Test for correct creation of amenity"""
        state = State(name="California")
        state.save()
        city = City(state_id=state.id, name="San Francisco")
        city.save()
        user = User(email="john@snow.com", password="johnpwd")
        user.save()
        place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
        place_1.save()
        place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
        place_2.save()
        amenity_1 = Amenity(name="Wifi")
        amenity_1.save()
        amenity_2 = Amenity(name="Cable")
        amenity_2.save()
        amenity_3 = Amenity(name="Oven")
        amenity_3.save()
        place_1.amenities.append(amenity_1)
        place_1.amenities.append(amenity_2)
        place_2.amenities.append(amenity_1)
        place_2.amenities.append(amenity_2)
        place_2.amenities.append(amenity_3)
        storage.save()
        obj = storage.all()
        self.assertIsNotNone(obj)

if __name__ == "__main__":
    unittest.main()
