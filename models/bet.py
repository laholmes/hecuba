from base import Base
from peewee import *
from status import Status
from account import Account

class Bet(Base):
    game_id = IntegerField()
    amount = DecimalField()
    proportion = DecimalField()
    percentage_win = DecimalField()
    odds = DecimalField(null=True)
    date = DateField()
    status = ForeignKeyField(Status, related_name='status')
    account = ForeignKeyField(Account, related_name='account')
