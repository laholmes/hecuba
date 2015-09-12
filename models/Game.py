from BaseModel import BaseModel
from peewee import *
from Team import Team

class Game(BaseModel):
    home_team_id = ForeignKeyField(Team, related_name='homeTeam')
    away_team_id = ForeignKeyField(Team, related_name='awayTeam')
    result = IntegerField()
