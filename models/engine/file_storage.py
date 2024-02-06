#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the list of objects of one type of class.
        it’s an optional filtering"""
        if cls is not None:
            class_dict = {}
            for key, value in FileStorage.__objects.items():
                if value.__class__ == cls:
                    class_dict[key] = value
            return class_dict
        return FileStorage.__objects

    def get(self, cls, id):
        """retrieves an object of a class with id"""
        if cls is not None:
            res = list(
                filter(
                    lambda x: type(x) is cls and x.id == id,
                    self.__objects.values()
                )
            )
            if res:
                return res[0]
        return None

    def count(self, cls=None):
        """retrieves the number of objects of a class or all (if cls==None)"""
        return len(self.all(cls))

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it’s
        inside - if obj is equal to None, the method should not do anything
        """
        if obj is not None:
            del FileStorage.__objects[obj.to_dict()['__class__'] + '.' +
                                      obj.id]
            self.save()
        else:
            pass

    def close(self):
        """Deserializing the JSON file to objects"""
        self.reload()
