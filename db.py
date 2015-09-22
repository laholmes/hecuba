from models.bet import Bet
from peewee import *
from models.bet import Bet

DATABASE = 'hecuba.db'
database = SqliteDatabase(DATABASE)

def create_tables():
    database.connect()
    database.create_tables([Bet])
