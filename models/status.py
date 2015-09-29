from base import Base
from peewee import *

class Status(Base):
    name = CharField()
