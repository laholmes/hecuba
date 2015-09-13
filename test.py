import nfldb
import json
from pprint import pprint

db = nfldb.connect()
q = nfldb.Query(db)

threshold = 0.03

# filtering
# returns all games in a gameweek with edge (538 vs betfair price) > threshold

with open("538.json") as data_file:
    data = json.load(data_file)

    q.game(season_year=2015, season_type='Regular', week=1)
    for g in q.as_games():

        betfairPriceHome = data["weeks"]["1"]["games"][g.gsis_id]["betfairPriceHome"]
        betfairPriceAway = data["weeks"]["1"]["games"][g.gsis_id]["betfairPriceAway"]
        homeTeamWeighting = data["weeks"]["1"]["games"][g.gsis_id]["homeTeamWeighting"]
        awayTeamWeighting = data["weeks"]["1"]["games"][g.gsis_id]["awayTeamWeighting"]

        betfairHomePercentage = 1 / (betfairPriceHome + 1)
        betfairAwayPercentage = 1 / (betfairPriceAway + 1)

        if(betfairHomePercentage >= homeTeamWeighting + threshold):
            print("found home team match!")

        if(betfairAwayPercentage >= awayTeamWeighting + threshold):
            print("found away team match!")

        print data["weeks"]["1"]["games"][g.gsis_id], g

# constructs list of bets for week with edge
