from base import Base
from peewee import *

class Account(Base):
    name = CharField()
    bankroll = FloatField()
    threshold = FloatField()
