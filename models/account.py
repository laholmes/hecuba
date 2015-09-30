from base import Base
from peewee import *

class Account(Base):
    name = CharField()
    bankroll = DecimalField()
    threshold = DecimalField()
