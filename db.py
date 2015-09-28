from models.bet import Bet
from peewee import *
from models.bet import Bet

DATABASE = 'hecuba.db'
database = SqliteDatabase(DATABASE)

def initialize():
    """Create the database and the table if they don't exist."""
    database.connect()
    database.create_tables([Bet], safe=True)