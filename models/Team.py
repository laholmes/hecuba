from BaseModel import BaseModel
from peewee import *

class Team(BaseModel):
    name = CharField()
