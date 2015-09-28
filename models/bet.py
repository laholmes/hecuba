from base import Base
from peewee import *

class Bet(Base):
    game_id = IntegerField()
    amount = DecimalField()
    proportion = DecimalField()
    odds = DecimalField(null=True)
    date = DateField()
    won = BooleanField(null= True)
