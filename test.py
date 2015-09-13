import nfldb
import json
from pprint import pprint
import betting

db = nfldb.connect()
q = nfldb.Query(db)

threshold = 0.04
bets = []
bankroll = 100

# returns all games in a gameweek with edge (538 vs betfair price) > threshold
with open("538.json") as data_file:
    data = json.load(data_file)

    q.game(season_year=2015, season_type='Regular', week=1)
    for g in q.as_games():
        betfairPriceHome = data["weeks"]["1"]["games"][g.gsis_id]["betfairPriceHome"]
        betfairPriceAway = data["weeks"]["1"]["games"][g.gsis_id]["betfairPriceAway"]
        homeTeamWeighting = data["weeks"]["1"]["games"][g.gsis_id]["homeTeamWeighting"]
        awayTeamWeighting = data["weeks"]["1"]["games"][g.gsis_id]["awayTeamWeighting"]

        betfairHomePercentage = 1.0 / (betfairPriceHome + 1)
        betfairAwayPercentage = 1.0 / (betfairPriceAway + 1)

        if(betfairHomePercentage + threshold <= homeTeamWeighting):
            bets.append({
                "team": "home",
                "gameId": g.gsis_id,
                "netOdds": betfairPriceHome,
                "percentageWin": homeTeamWeighting
            })

        if(betfairAwayPercentage + threshold <= awayTeamWeighting):
            bets.append({
                "team": "away",
                "gameId": g.gsis_id,
                "netOdds": betfairPriceAway,
                "percentageWin": awayTeamWeighting
            })

for bet in bets:
    bet["size"] = betting.KellySize(bet["netOdds"], bet["percentageWin"], bankroll)
    print(bet)
