from models.bet import Bet
from models.status import Status
from models.account import Account
from peewee import *

DATABASE = 'hecuba.db'
database = SqliteDatabase(DATABASE)

def seed_data():
    states = [
        {'name': 'pending'},
        {'name': 'placed'},
        {'name': 'cancelled'},
        {'name': 'won'},
        {'name': 'lost'}]
    for state in states:
        Status.insert(**state)

    Account.insert(**{
        'name': 'primary',
        'bankroll': 100,
        'threshold': 0.04
    })

def initialize():
    """Create the database and the table if they don't exist."""
    database.connect()
    database.create_tables([Bet, Status, Account], safe=True)
    seed_data()
