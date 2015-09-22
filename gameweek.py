import nfldb
import json
from pprint import pprint
import betting
from models.bet import Bet
import datetime

db = nfldb.connect()
q = nfldb.Query(db)

q.game(season_year=2015, season_type='Regular', week=2)
for g in q.as_games():
    print(g.gsis_id)
    print(g)
