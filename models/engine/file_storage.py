#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            objdict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    objdict[key] = value
            return objdict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for obj in json.load(file).values():
                    name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(name)(**obj))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete object obj from object dictionary __objects"""
        if not obj:
            return
        the_key = "{}.{}".format(type(obj).__name__, obj.id)
        if the_key in self.__objects:
            del self.__objects[the_key]
            self.save()

    def close(self):
        """refresh the object dictionary with new contents"""
        self.reload()
