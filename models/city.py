#!/usr/bin/python3
"""DEFINING CITY CLASS."""
from models.base_model import BaseModel


class City(BaseModel):
    """FOR CITY .

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
