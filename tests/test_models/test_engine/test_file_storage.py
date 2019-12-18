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
from models.engine.file_storage import FileStorage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "DBStorage Mode")
class TestFileStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = FileStorage()
        cls.state = State(name="Cundinamarca")

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user
        del cls.state

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_all_cls(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        new_city = City(name="Bogota")
        city_id = new_city.id
        storage.new(new_city)
        storage.save()
        obj_city = storage.all(City)
        self.assertIsNotNone(obj_city)
        self.assertEqual(type(obj_city), dict)
        self.assertEqual(len(obj_city), 2)
        city = obj_city["City." + city_id]
        self.assertEqual(city.id, city_id)

    def test_delete(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        state_instance = State(name="California")
        self.assertIsNotNone(state_instance)
        storage.new(state_instance)
        storage.save()
        storage.delete(state_instance)
        obj_state = storage.all(State)
        self.assertEqual(len(obj_state), 0)

    def test_new(self):
        """test when new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
