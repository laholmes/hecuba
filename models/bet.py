from base import Base
from peewee import *

class Bet(Base):
    game_id = IntegerField()
    amount = DecimalField()
    odds = DecimalField()
    date = DateField()
    won = BooleanField(null= True)
