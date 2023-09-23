#!/usr/bin/python3
# Auth: codenvibes
"""
This module defines a base class.
"""
import json


class Base:
    """
    This is the base class.

    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): A list of dictionaries to be
            converted to JSON.

        Returns:
            str: A JSON-formatted string representing the input list of
            dictionaries.
                If the input is empty or None, an empty JSON array "[]" is
                returned.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file named after the class.

        Args:
            cls (class): The class calling this method.
            list_objs (list): A list of objects to be saved to the JSON file.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))
