#!/usr/bin/python3

"""this defines the Amenity class."""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
