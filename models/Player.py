from BaseModel import BaseModel
from peewee import *
from Team import Team

class Player(BaseModel):
    first_name = CharField()
    last_name = CharField()
    dob = DateField()
    team_id = ForeignKeyField(Team, related_name='team')
